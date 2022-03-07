from django.contrib import admin

from . models import TodoList, ToDoItem

admin.site.register(TodoList)
admin.site.register(ToDoItem)
