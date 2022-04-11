from django.core.mail import EmailMessage

def send_todo_mail(email,token):   
    """ Sending users email when they completed todos"""
    print("Email ve Token",email,token)
    print("Email is preparing")
    link = f"http://127.0.0.1:8000/todo/todos/{token}/"
    subject = "You created a new todo. Visit your todo"
    recipients = [email]
    send_email = EmailMessage(subject=subject, body=link, from_email="rapor@scor-app.com",to=recipients)
    send_email.send()
    print("Email sent")