from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request,id=None):
    tasks = Task.objects.all()

    
    if id:
        complete_task(id)
        return redirect('/')

    return render(request,'todo_app/home.html',{'tasks':tasks})


def add_task(request):
    """add new task"""
    if request.method == "POST":

        if request.POST.get('name') != '':
            name = request.POST.get('name')
            priority = request.POST.get('priority')
            due_date= request.POST.get('date')
            task = Task(name=name,priority=priority,date=due_date)
            task.save()

      
            return redirect('/')
        else:

            msg = 'Please enter the task name.'
            tasks = Task.objects.all()
            return render(request,'todo_app/home.html',{'msg':msg, 'tasks':tasks})

def complete_task(id):

    task = Task.objects.get(id=id)
    task.delete()
     
        