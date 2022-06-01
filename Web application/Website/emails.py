import datetime as dt
import time
import smtplib

def send_email(message):
    email_user = 'testcmt0@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'testuniemail1')

    server.sendmail(email_user, email_user, message)
    server.quit()