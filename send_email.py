import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(msg):
    host = 'smtp.google.com'
    port = 465
    user = os.getenv('EMAIL')
    pw = os.getenv('PW')
    context = ssl.create_default_context()
    receiver = 'prowlersk8@gmail.com'

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user, pw)
        print('Logged In')
        server.sendmail(user, receiver, msg)
        print('Sent')
