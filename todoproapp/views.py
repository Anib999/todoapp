from django.shortcuts import render
from .models import Todomodel
from django.http import HttpResponseRedirect
# Create your views here.

def todoView(request):
    modelList = Todomodel.objects.all()
    context = {'todoList': modelList}
    return render(request, 'todolist.html', context)

def addTodoItem(request):
    x = request.POST['content']
    new_item = Todomodel(content=x)
    new_item.save()
    return HttpResponseRedirect('/')

def deleteContent(request, pk):
    y = Todomodel.objects.get(id=pk)
    y.delete()
    return HttpResponseRedirect('/')

def editContent(request,pk):
    y = Todomodel.objects.get(id=pk)
    context = {'todoList': y}
    return render(request, 'todolist.html', context)