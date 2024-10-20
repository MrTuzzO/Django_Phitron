import datetime
from django import forms


FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class formsApi(forms.Form):
    name = forms.CharField(initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Please enter your email address",)
    agree = forms.BooleanField()
    date = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_multiple_select = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)


