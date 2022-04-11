from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Todo

from .serializers import TodoSerializer

from .permissions import IsOwner

class TodoView(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


