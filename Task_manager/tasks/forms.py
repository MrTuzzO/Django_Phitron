from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['is_completed']

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'