import smtplib
from email.message import EmailMessage
import os
import celery
from celery.schedules import crontab
from app import celery_app


@celery_app.task(name="send_emails")
def send_emails():
    email = "pritigopal408@gmail.com"
    sender = "pratikgopal.cha26@gmail.com"
    # password = os.getenv("EMAIL_PASSWORD")
    password = "senaanyjoxlmtjoq"

    receiver = email
    print(receiver)
    subject = "This is a test email"
    body = "Take Care of your health"

    em = EmailMessage()
    em['From'] = "pratikgopal.cha26@gmail.com"
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        print("Testing this one")
        smtp.sendmail(sender, receiver, em.as_string())
        print("Sending email smtp")

    return True
