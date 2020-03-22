from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:note_id>/detail/', views.todo_detail, name="todo_detail"),
    path('create/', views.todo_create, name="todo_create"),
]