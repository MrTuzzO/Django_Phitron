from django.shortcuts import render
from . import forms
# Create your views here.
def formsapi(request):
    return render(request, 'forms.html', {'form': forms.formsApi})
