from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Labas, autoserviso naudotojau!")

# Create your views here.
