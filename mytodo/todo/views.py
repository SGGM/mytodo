from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView

from .models import Todo
from .forms import TodoForm



# class TodoList(ListView):
#     """Main page with all todos"""
#     model = Todo
#     template_name = 'todo_list.html'


def todo_view(request):
    dataset = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'dataset': dataset})


def todo_detail_view(request, id):
    try:
        data = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        raise Http404("Page not found ;(")

    return render(request, 'todo/todo_detail.html', {'data': data})


def create_todo_view(request):
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm
        context = {
            'form': form
        }
        return render(request, 'todo/create_todo.html', context)


def todo_update(request, id):
    try:
        old_data = get_object_or_404(Todo, id=id)
    except Exception:
        raise Http404('Todo doesn\'t exist')
    if request.method =='POST':
        form = TodoForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance = old_data)
        context ={
            'form':form
        }
        return render(request, 'todo/update_todo.html', context)


def todo_delete(request, id):
    try:
        data = get_object_or_404(Todo, id=id)
    except Exception:
        raise Http404('Todo doesn\'t exist')
 
    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        return render(request, 'todo/delete_todo.html')