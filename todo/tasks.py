from celery import shared_task
from .send_mail import send_todo_mail

@shared_task
def send_mail_with_celery(email,token):
    send_todo_mail(email,token)