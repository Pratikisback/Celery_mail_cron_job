import smtplib
from email.message import EmailMessage


def send_emails(email):
    sender = "pratikgopal.cha26@gmail.com"
    password = "sena anyj oxlm tjoq"

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