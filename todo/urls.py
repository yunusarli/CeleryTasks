from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = "todo"
router = DefaultRouter()
router.register("todos",views.TodoView,basename="todos")

urlpatterns = [
    path("",include(router.urls),name="todos"),
]