from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Uzsakymas, UzsakymoEilute, Modelis, Automobilis
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    num_uzsakymas = Uzsakymas.objects.all().count()  # is models.py, Book klases
    num_uzsakymo_eilute = UzsakymoEilute.objects.all().count()
    num_modelis = Modelis.objects.all().count()
    # Filtruojame is kintamojo status 'g' reiksme
    num_instances_g = Uzsakymas.objects.filter(status__exact='g').count()
    times_visited = request.session.get('num_of_visits', 1)
    request.session['num_of_visits'] = times_visited + 1
    context = {'num_uzsakymas': num_uzsakymas,
               'num_uzsakymo_eilute': num_uzsakymo_eilute,
               'num_modelis': num_modelis,
               'num_instances_g': num_instances_g,
               'num_of_visits': times_visited}
    return render(request, 'index.html', context=context)


def modeliai(request):
    modeliai_num = Modelis.objects.all()
    context = {'modeliai_num': modeliai_num,
               }
    return render(request, 'modeliai.html', context=context)


def automobiliai(request):
    # automobiliai_num = Automobilis.objects.all()
    paginator = Paginator(Automobilis.objects.all(), 3)
    page_number = request.GET.get('page')
    paged_automobiliai = paginator.get_page(page_number)
    context = {'automobiliai_num': paged_automobiliai,
               }
    return render(request, 'automobiliai_with_pics.html', context=context)


def automobile(request, auto_id):
    single_auto = get_object_or_404(Automobilis, pk=auto_id)  # pk - primary key
    return render(request, 'auto.html', {'auto_automobile': single_auto})


def search(request):
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(
                        Q(valstybinis_numeris__icontains=query) | Q(klientas__icontains=query) |
                        Q(vin_kodas__icontains=query) |
                        Q(automobilio_modelis_id__marke__icontains=query) |
                        Q(automobilio_modelis_id__modelis__icontains=query)
    )
    return render(request, 'search.html', {"autos_search": search_results, "query": query})


class OrdersListView(generic.ListView):
    model = UzsakymoEilute
    paginate_by = 5
    template_name = 'uzsakymai_eilutes.html'
    context_object_name = 'uzsakymai_num'

# def orders(request):
#     uzsakymai_num = UzsakymoEilute.objects.all()
#     context = {'uzsakymai_num': uzsakymai_num}
#     return render(request, 'uzsakymai_eilutes.html', context=context)


class OrderDetailView(generic.DetailView):
    model = UzsakymoEilute
    template_name = "uzsakymas_detail_view.html"

# def orders_order(request, ue_id):
#     single_ue = get_object_or_404(UzsakymoEilute, pk=ue_id)  # pk - primary key
#     return render(request, 'uzsakeil_detail.html', {'uzsakeil_single': single_ue})