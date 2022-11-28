from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def list_tasks(request):
    tasks= Task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})


#al darle enviar llega como request, desde ahi se usa Task para guardar dato por dato en task y luego salvarlo en la db
def create_task(request):
    task= Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')