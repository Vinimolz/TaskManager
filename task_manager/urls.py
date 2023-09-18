from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('temp', views.temp, name="temp"),
    path('create_task', views.create_task, name="create_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
]