import django_filters
from django_filters import CharFilter

from .models import TodoList, ToDoItem

class TodoListFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')

    class Meta:
        model = TodoList
        fields = ['title']

class ToDoItemFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')

    class Meta:
        model = ToDoItem
        fields = ['title']


