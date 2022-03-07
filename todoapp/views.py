from django.shortcuts import render, redirect

from . models import ToDoItem, TodoList
from . filters import TodoListFilter, ToDoItemFilter
from .forms import PostForm, CrudForm

def home(request):
    todoList = TodoList.objects.filter(active=True, featured=True)[0:6]
    context = {
        'todoList': todoList
    }
    return render(request, 'todoapp/index.html', context)

def todoItemView(request):
    listItems = ToDoItem.objects.filter(active=True)
    myFilter = ToDoItemFilter(request.GET, queryset=listItems)
    listItems = myFilter.qs
    context = {
        'listItems': listItems,
        'myFilter': myFilter
    }
    return render(request, 'todoapp/listItem.html', context)

def todoListView(request, slug):
    todoList = TodoList.objects.get(slug=slug)
    myFilter = TodoListFilter(request.GET, queryset=todoList)
    context = {
        'todoList': todoList,
        'myFilter': myFilter
    }
    return render(request, 'todoapp/toDoList.html', context)


def createTask(request):
    form = PostForm

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('list_items')

    context = {
        'form': form
    }
    return render(request, 'todoapp/post_form.html', context)
def updateList(request, slug):
    updateList = TodoList.objects.get(slug=slug)
    form = CrudForm(instance=updateList)

    if request.method == 'POST':
        form = CrudForm(request.POST, request.FILES, instance=updateList)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'todoapp/toDoList.html', context)


def updateTask(request, slug):
    listItems = ToDoItem.objects.get(slug=slug)
    form = PostForm(instance=listItems)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=listItems)
        if form.is_valid():
            form.save()
        return redirect('list_items')

    context = {
        'form': form
    }
    return render(request, 'todoapp/post_form.html', context)

def deleteTask(request, slug):
    todoItem = ToDoItem.objects.get(slug=slug)

    if request.method == 'POST':
        todoItem.delete()
        return redirect('list_items')

    context = {
        'item': todoItem
    }
    return render(request, 'todoapp/delete.html', context)

def deleteList(request, slug):
    todoList = TodoList.objects.get(slug=slug)
    if request.method == 'POST':
        todoList.delete()
        return redirect('home')
    context = {
        'item': todoList,
    }
    return render(request, 'todoapp/deleteTask.html', context)