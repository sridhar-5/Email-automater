# import the smtplib module.
import smtplib
from decouple import config
import getContacts
import template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# setting up the smtp server
server = smtplib.SMTP(host="smtp.gmail.com", port=587)

server.starttls()
# enter your mail details
USER_EMAIL = config("EMAIL")
USER_PASSWORD = config("PASSWORD")
server.login(USER_EMAIL, USER_PASSWORD)

names, emails = getContacts.getContacts()
message_template = template.readTemplate()

for name, email in zip(names, emails):
    # Creating message here
    Message = MIMEMultipart()

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setting up the parameters for the email
    Message["From"] = config("EMAIL")
    Message["To"] = email
    Message["Subject"] = "Welcome SPOCs!"

    # add the message body to the mail
    Message.attach(MIMEText(message, 'plain'))
    server.send_message(Message)
    print("Mail sent to: ", email)
    del Message

