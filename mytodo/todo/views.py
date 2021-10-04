from django.http.response import Http404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Todo
from .forms import TodoForm



# class TodoList(ListView):
#     """Main page with all todos"""
#     model = Todo
#     template_name = 'todo_list.html'


def todo_view(request):
    dataset = Todo.objects.all()
    return render(request, 'todo_list.html', {'dataset': dataset})


def todo_detail_view(request):
    try:
        data = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Page not found ;(")

    return render(request, 'todo_list.html', {'data': data})


def create_todo_view(request):
    
    if request.method == 'POST':
        form = TodoForm
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm
        context = {
            'form': form
        }
        return render(request, 'create_todo.html', context)