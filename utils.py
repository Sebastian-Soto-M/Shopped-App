import os
import smtplib
import json
import string
import secrets
from email.message import EmailMessage

from main import bcrypt

import requests


def get_url(url: str) -> dict:
    response = requests.get(url)
    return json.loads(response.text)


def put(url: str, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.put(url, json=data, headers=headers)


def post(url: str, data):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return requests.post(url, json=data, headers=headers)


def new_password() -> str:
    alphabet = string.ascii_letters + string.digits
    passwd = "".join(secrets.choice(alphabet) for i in range(8))
    return (passwd, bcrypt.generate_password_hash(passwd).decode('utf-8'))


def send_mail(name, email, subject, msg):
    mail = EmailMessage()
    mail['Subject'] = subject
    mail['From'] = os.environ['EMAIL_ADDRESS']
    mail['To'] = email
    mail.set_content(f'{name}:\t{email}\n\n{msg}')
    mail.add_alternative(f"""
        <!DOCTYPE html>
        <html lang="en">

        <body>
            <div style="margin: 1rem; ">
                <div style="text-decoration: none; text-align: center; line-height: 1.15rem; margin-bottom: 1rem;">
                    <h1 style="text-transform: capitalize; margin: 0px">{name}</h1>
                </div>
                <div style="padding: 0.5rem; border: 1px solid rgba(100,100,100,0.5);">
                    <p style="margin: 0px; padding: 1rem;">{msg}</p>
                </div>
            </div>
        </body>

        </html>
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        smtp.send_message(mail)
