from django import forms
from . import models

class model_Form(forms.ModelForm):
    class Meta:
        model = models.modelForm
        fields = '__all__'