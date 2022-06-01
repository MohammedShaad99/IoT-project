from flask import render_template, url_for, flash, redirect, request, abort
from Website import app, db, bcrypt
from Website.forms import RegistrationForm, LoginForm
from Website.models import User, RoomInfo, Room
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from joblib import load
import os
from Website.emails import send_email
import smtplib
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
#to enable flask admin
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Room, db.session))
admin.add_view(ModelView(RoomInfo, db.session))
#global vars 
cwd = os.getcwd()
#loading the novelty detection classifier
novelty_clf = load(cwd + "/Website/models/novelty_detector.joblib")
webhookdata = []

#deals with web hooks,quieres the database for latest room info entry
@app.route("/",methods = ['POST', 'GET'])
@app.route("/home",methods = ['POST', 'GET'])
def home():
    global webhookdata
    global novelty_clf
    if request.method == 'POST':
        print(request.json)
        for requestDict in request.json:
            webhookdata = RoomInfo(room_id = requestDict['room_id'], liveCapacity = requestDict['liveCapacity'],
                                   temp = requestDict['temp'], sound = requestDict['sound'], humdity = requestDict['humdity'], light = requestDict['light'],)
            db.session.add(webhookdata)
            db.session.commit()
            clf_result = novelty_clf.predict([[requestDict['temp'], requestDict['humdity']]])
            if clf_result == -1:
                errorstr = 'strange detected, current temp in room id:'+ str(requestDict['room_id']) + ' is: '+  str(requestDict['temp'])+ 'and humidity:' +str(requestDict['humdity'])
                send_email(errorstr)
                
            print(webhookdata)
        return 'success', 200 
    elif (request.method == 'GET'):
        rooms = Room.query.all()
        print(rooms)
        return render_template('home.html', rooms = rooms, roominfo= RoomInfo)
    else:
        abort(400)

#directs users to a datastudio enabled html page
@app.route("/Analytics")
def Analytics():
    return render_template('Analytics.html', title='Analytics')

#hashed regestration
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

#encrypted login
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')