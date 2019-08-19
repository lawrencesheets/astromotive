from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import BaseForm

from .models import Greeting

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = BaseForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
    form = BaseForm()

    return render(request, "index.html", {'form': form})



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
