from rest_framework import serializers
from fileupload.models import TemporaryExcelKeeper

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryExcelKeeper
        fields = "__all__"