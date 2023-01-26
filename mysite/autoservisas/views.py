from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Uzsakymas, UzsakymoEilute, Modelis, Automobilis
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin, CreateView, UpdateView, DeleteView
from .forms import UzsakymasReviewForm, UserUpdateForm, ProfilisUpdateForm, UserOrderCreateForm
from django.contrib.auth.decorators import login_required


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
    paginator = Paginator(Automobilis.objects.all(), 2)
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


class OrderDetailView(FormMixin, generic.DetailView):
    model = UzsakymoEilute
    template_name = "uzsakymas_detail_view.html"
    form_class = UzsakymasReviewForm

    # nustatome settings
    class Meta:
        ordering = ['paslauga_id']

    # Nukreipimas po sekmingo komentaro parasymo atgal i knygos langa
    def get_success_url(self):
        return reverse('uzsakeil-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.order_line = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)

# def orders_order(request, ue_id):
#     single_ue = get_object_or_404(UzsakymoEilute, pk=ue_id)  # pk - primary key
#     return render(request, 'uzsakeil_detail.html', {'uzsakeil_single': single_ue})


class OrderDetailByUserListView(LoginRequiredMixin, generic.ListView):  # Paveldime is dvieju klasiu!
    model = UzsakymoEilute  # gausime context={'bookinstance_list': BookInstance}
    template_name = 'uzsakymas_detail_view_user.html'

    # perrasome metoda get_queryset is klases generic.ListView. Child klases metodas veiks kreipiantis per Child klase
    # filter(reader=self.request.user) - isrenka useri
    # filter(status_exact='p') - isrenka BookInstance statusus su 'p' raktu
    # order_by('due_back') - surusiuoja pagal data
    def get_queryset(self):
        return UzsakymoEilute.objects.filter(useris=self.request.user).order_by('grazinti_iki')


@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} yra uzimtas')
                return redirect('registration')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Emailas {email} yra uzimtas kito vartotojo')
                    return redirect('registration')
                else:
                    User.objects.create_user(username=username, email=email, password=password1)
                    messages.info(request, f'Vartotojas {username} sekmingai uzregistruotas')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptazodzia nesutampa')
            return redirect('registration')

    return render(request, 'register.html')


@login_required
def profilis(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.info(request, "Profilis sekmingai atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profilis.html', context=context)


class UzsakymoEiluteByUserCreateView(LoginRequiredMixin, CreateView):
    model = UzsakymoEilute
    # fields = '__all__'  # rodo visus modelio laukus, bet jeigu nori isskirti ka rodysime, turime daryti kaip zemiau
    # fields = ('book', 'due_back', 'status')  - Prijungsime laukus is forms.py todel sitie nereikalingi
    success_url = '/autoservisas/myorders/'  # kur nukreipsime po sekmingo posto
    template_name = 'user_order_form.html'
    form_class = UserOrderCreateForm

    def form_valid(self, form):
        form.instance.useris = self.request.user
        return super().form_valid(form)


class UzsakymoEiluteByUserDetailView(LoginRequiredMixin, OrderDetailView):
    model = UzsakymoEilute
    template_name = 'user_order.html'


# LogisRequiredMixin - kas tik isilogines galetu daryt dalykus
# UserPassesTestMixin - kad isilogines useris negaletu keisti dalyku kitu useriu vardu
# Update View - kad useris galetu keisti dalykus
class UzsakymoEiluteByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UzsakymoEilute
    fields = ('kiekis', 'paslauga_id')
    success_url = '/autoservisas/myorders/'  # kur nukreipsime po sekmingo keitimo
    template_name = 'user_order_form.html'

    def form_valid(self, form):
        form.instance.useris = self.request.user
        return super().form_valid(form)

    def test_func(self):
        uzsakymasinstance = self.get_object()
        return self.request.user == uzsakymasinstance.useris  # testas ar prisijunges useris atitinka to instance, kuri
        # norime keisti "savininka". Cia, kad kitas useris nekeistu kito userio pakeitimu.


class UzsakymoEiluteByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UzsakymoEilute
    success_url = '/autoservisas/myorders/'
    template_name = 'user_order_delete.html'

    def test_func(self):
        uzsakymasinstance = self.get_object()
        return self.request.user == uzsakymasinstance.useris