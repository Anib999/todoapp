from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoView, name="todoView"),
    path('addTodoItem/', views.addTodoItem, name="addTodoItem"),
    path('deleteContent/<int:pk>', views.deleteContent, name="deleteContent"),
    path('editContent/<int:pk>', views.editContent, name="editContent"),
]