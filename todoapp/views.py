from django.shortcuts import render,redirect
from todoapp.models import Todo

# Create your views here.


def home_view(request):
    todo_list=Todo.objects.all()
    context={
        'todo_list':todo_list
    }

    return render(request,"home.html",context)


def add_task(request): #task="Playing cricket"
    t=Todo(task=request.POST.get('task'))
    t.save()
    return redirect("/home")




def delete_one_data(request,id):
    one_task=Todo.objects.get(id=id)
    one_task.delete()
    return redirect("/home")














