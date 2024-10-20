from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    person = {
        "name" : "Khirul Islam",
        "age" : 22,
        "marks" : [70, 60, 86, 91, 56, 80],
        "friends": ["Karim", "Zoy", "Pial", "Nayeem", "Najmul"],
        "currentTime" : datetime.datetime.now(),
        "sentence":"hello, i am learning pyhton django framework."
    }
    return render(request, 'index.html',person)