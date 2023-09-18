from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Task
from .forms import TaskForm, AppUserForm
from .task_handler import TaskManager

def sign_up(request):
    if request.method == 'POST':
        form = AppUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('temp')
        
    else:
        form = AppUserForm()

    return render(request, 'task_manager/sign_up.html', {'form': form})

def temp(request):
    return render(request, 'task_manager/temp.html')

def home(request):
    tasks = Task.objects.filter(assigned_to=request.user)

    context_dict = {
        'tasks': tasks,
    }
    
    return render(request, 'task_manager/home.html', context_dict)

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            
            # Authenticated user
            user = request.user
            
            # Create instance of taskmanager to handle task creation            
            task_manager = TaskManager(user)

            task_manager.create_task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                due_date=form.cleaned_data['due_date'],
                assigned_to=form.cleaned_data['assigned_to'],
            )

            return redirect('home')
        
    else:
        form = TaskForm()

    return render(request, 'task_manager/create_task.html', {'form': form})

def delete_task(request, task_id):
    task_manager = TaskManager(request.user)

    if task_manager.delete_task(task_id):
        print("Task Deleted")
    else:
        print("Problem deleting task")

    return redirect('home')