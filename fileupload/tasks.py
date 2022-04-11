from celery import shared_task
from .import_export import SaveFileToDatabase

@shared_task
def celery_upload_file_task(user_id,url):
    SaveFileToDatabase(user_id,url).uplaod_to_database()