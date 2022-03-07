from django.forms import ModelForm

from .models import ToDoItem, TodoList

class PostForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = '__all__'

class CrudForm(ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'