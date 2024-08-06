from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            title = request.POST['title']
            Task.objects.create(title=title)
        elif 'update' in request.POST:
            task_id = request.POST['task_id']
            task = get_object_or_404(Task, id=task_id)
            task.title = request.POST['title']
            task.completed = 'completed' in request.POST  # Update the completed status based on form data
            task.save()
        elif 'delete' in request.POST:
            task_id = request.POST['task_id']
            task = get_object_or_404(Task, id=task_id)
            task.delete()
        elif 'toggle' in request.POST:
            task_id = request.POST['task_id']
            task = get_object_or_404(Task, id=task_id)
            task.completed = not task.completed  # Toggle the boolean value
            task.save()
        return redirect('index')

    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})
