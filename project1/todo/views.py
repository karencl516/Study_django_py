from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm


def home (request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'todo/home.html', context)

def add (request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm()
    context = {'form':form}
    return render(request, 'todo/add.html',context)

def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("home")

def edit (request,task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    context = {'form':form}
    return render(request, 'todo/edit.html',context)
