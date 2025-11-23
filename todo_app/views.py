from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoItem

class TodoListView(ListView):
    model = TodoItem
    template_name = 'todo_app/todo_list.html'
    context_object_name = 'todos'
    ordering = ['due_date']

class TodoCreateView(CreateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date']
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = TodoItem
    fields = ['title', 'description', 'due_date']
    template_name = 'todo_app/todo_form.html'
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'todo_app/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')

def toggle_resolved(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.is_resolved = not todo.is_resolved
    todo.save()
    return redirect('todo-list')
