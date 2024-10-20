from django.shortcuts import render
from . import forms
def modelsForm(request):
    return render(request, 'modelsForm.html', {'form': forms.model_Form})