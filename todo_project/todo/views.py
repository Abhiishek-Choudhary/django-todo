from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def deleteTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('/')

def toggleTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect('/')

