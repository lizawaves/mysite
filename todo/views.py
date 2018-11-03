from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})

def addTodo(request):

    #create a new_items
    new_item = TodoItem(content = request.POST['content'])

    # save
    new_item.save()

    # redirect to the browser
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):

    #find the item do delete
    item_to_delete = TodoItem.objects.get(id=todo_id)

    #delete
    item_to_delete.delete()

    # redirect to the browser
    return HttpResponseRedirect('/todo/')