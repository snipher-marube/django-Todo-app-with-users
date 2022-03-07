from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_items/', views.todoItemView, name='list_items'),
    path('todoList/<slug:slug>/', views.todoListView, name='todoList'),

    #CRUD
    path('create_task/', views.createTask, name='create_task'),
    path('update_task/<slug:slug>/', views.updateTask, name='update_task'),
    path('delete_task/<slug:slug>/', views.deleteTask, name='delete_task'),
    path('update_list/<slug:slug>', views.updateList, name='update_list'),
    path('delete_list/<slug:slug>', views.deleteList, name='delete_list'),
]