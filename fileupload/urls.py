from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "file_uplaod"

router = DefaultRouter()
router.register("upload",views.FileUploadView,basename="uploading_files")

urlpatterns = [
    path("",include(router.urls))
]