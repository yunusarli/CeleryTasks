from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response


from fileupload.models import TemporaryExcelKeeper

from .serializers import FileUploadSerializer

class FileUploadView(viewsets.ModelViewSet):
    queryset = TemporaryExcelKeeper.objects.all()
    serializer_class = FileUploadSerializer

