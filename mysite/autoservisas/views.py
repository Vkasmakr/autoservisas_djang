from django.shortcuts import render
from django.http import HttpResponse
from .models import Uzsakymas, UzsakymoEilute, Modelis, Automobilis

def index(request):
    num_uzsakymas = Uzsakymas.objects.all().count()  # is models.py, Book klases
    num_uzsakymo_eilute = UzsakymoEilute.objects.all().count()
    num_modelis = Modelis.objects.all().count()
    # Filtruojame is kintamojo status 'g' reiksme
    num_instances_g = Uzsakymas.objects.filter(status__exact='g').count()
    context = {'num_uzsakymas': num_uzsakymas,
               'num_uzsakymo_eilute': num_uzsakymo_eilute,
               'num_modelis': num_modelis,
               'num_instances_g': num_instances_g}
    return render(request, 'index.html', context=context)


def modeliai(request):
    modeliai_num = Modelis.objects.all()
    context = {'modeliai_num': modeliai_num,
               }
    return render(request, 'modeliai.html', context=context)


def automobiliai(request):
    automobiliai_num = Automobilis.objects.all()
    context = {'automobiliai_num': automobiliai_num,
               }
    return render(request, 'automobiliai.html', context=context)
