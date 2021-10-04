from django.urls import path

from .views import create_todo_view, todo_detail_view, todo_view



urlpatterns = [
    path('', todo_view, name='todo_list'),
    path('create/', create_todo_view, name='create_todo'),
    path('<int:id>', todo_detail_view, name='detail_todo'),
]
