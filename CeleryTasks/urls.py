"""CeleryTasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include
from django.conf.urls.static import static
from CeleryTasks.settings import MEDIA_ROOT, MEDIA_URL

def redirect_to_home(request):
    return redirect("/todo/todos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",redirect_to_home,name="redirect_to_home"),
    path("todo/",include("todo.urls")),
    path("file-upload/",include("fileupload.urls")),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
