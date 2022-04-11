from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_mail_with_celery


class Todo(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    description = models.TextField(blank=True,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


@receiver(post_save,sender=Todo)
def send_mail_to_user(sender,instance,created,**kwargs):
    if created:
        print("Email will be sent")
        token = instance.id
        email = instance.user.email
        send_mail_with_celery.delay(email,token)
    print("The process is done!")