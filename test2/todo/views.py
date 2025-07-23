from django.shortcuts import render, redirect
from .forms import AddTasks

tasks = ['learn django', 'study an exam', 'online classes']

def home(request):
    context = {'tasks': tasks}
    return render(request,"todo/home.html", context)

def add(request):
    if request.method == 'POST':
        form = AddTasks(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return  redirect('home')

    else:
        form = AddTasks()

    context = {'form':form}
    return  render(request, "todo/add.html", context)


