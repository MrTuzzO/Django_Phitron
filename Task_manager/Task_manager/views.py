from django.shortcuts import render
from tasks.models import TaskModel
def home(request):
    data = TaskModel.objects.all()
    return render(request, 'home.html', {'data': data})