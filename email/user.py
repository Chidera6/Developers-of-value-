from email.message import EmailMessage
from app import PASS
import ssl
import smtplib
import ast

with open ('user.txt', 'r') as f:
    email_sender = 'Onumajurubenedicta@gmail.com'
    email_password = PASS
    my_data = ast.literal_eval(f.read())
    for name,mail in my_data.items():
        email_receiver = name.get('user_email')
        subject = "Chidera Stella-Backend Developer "
        body = "My name is Chidera,A backend developer specializing on Python and Flask."
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
