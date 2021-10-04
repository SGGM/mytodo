from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Todo



class TodoList(ListView):
    model = Todo
    template_name = 'todo_list.html'
