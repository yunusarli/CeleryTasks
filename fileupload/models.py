from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from CeleryTasks.settings import BASE_DIR
from .tasks import celery_upload_file_task

class TemporaryExcelKeeper(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file = models.FileField(upload_to="temporary_keeper")

    def __str__(self):
        return self.file.name
    
    def get_file_name(self):
        return self.file.name



        

