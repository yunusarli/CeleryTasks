from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TemporaryExcelKeeper
from .tasks import celery_upload_file_task



@receiver(post_save,sender=TemporaryExcelKeeper)
def test_post_save_with_celery(sender,instance,created,**kwargs):
    if created:
        print(sender)
        celery_upload_file_task.delay(instance.user.id,instance.file.url)
        instance.delete()