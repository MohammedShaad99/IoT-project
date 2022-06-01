
from datetime import datetime
from sqlite3 import Timestamp
from Website import db, loginManager
from flask_login import UserMixin
from sqlalchemy.sql import func

#database models 

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    roomInfo = db.relationship('RoomInfo', backref='room', lazy=True)

class RoomInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'),nullable=False)
    timeStamp = db.Column(db.DateTime(timezone=True),server_default=func.now())
    liveCapacity = db.Column(db.Integer, nullable=False)
    temp = db.Column(db.Integer, nullable=False)
    sound = db.Column(db.String(50), nullable=False)
    humdity = db.Column(db.Integer, nullable=False)
    light = db.Column(db.String(50), nullable=False)
    