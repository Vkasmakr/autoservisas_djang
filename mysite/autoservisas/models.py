from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField

# Create your models here.


class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200, help_text='Iveskite paslaugos pavadinima')
    kaina = models.FloatField('Kaina', max_length=10, help_text='Iveskite paslaugos kaina')

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = "Paslaugos"

    def __str__(self):
        return f'{self.pavadinimas} - {self.kaina} EUR'


class UzsakymoEilute(models.Model):
    kiekis = models.CharField('Kiekis', max_length=2, help_text='Iveskite perkamos paslaugos kieki')
    kaina = models.FloatField('Kaina', max_length=10, help_text='Iveskite paslaugos kaina', default=0)
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True)
    useris = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    grazinti_iki = models.DateField('Pabaigti darbus iki: ', null=True, blank=True)

    @property
    def is_overdue(self):
        if self.grazinti_iki and date.today() > self.grazinti_iki:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('uzsakeil-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Uzsakymo eilute"
        verbose_name_plural = "Uzsakymo eilutes"

    def __str__(self):
        return f'{self.uzsakymas_id} - {self.kiekis} - {self.kaina}'


class Uzsakymas(models.Model):
    data = models.DateField('Uzsakymo data', null=True, blank=True)
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    suma = models.FloatField('Suma', max_length=10, help_text='Iveskite paslaugos kaina', default=0)
    LOAN_STATUS = (
        ('a', 'Uzsakymas gautas'),
        ('p', 'Uzsakymas priimtas'),
        ('g', 'Uzsakymas vykdomas'),
        ('r', 'Uzsakymas baigtas')
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Status'
    )

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        ordering = ['data']
        verbose_name = "Uzsakymas"
        verbose_name_plural = "Uzsakymai"

    def __str__(self):
        return f'Uzsakymo data: {self.data} - {self.automobilis_id} - {self.suma}'


class Automobilis(models.Model):
    valstybinis_numeris = models.CharField('Automobilio valstybinis numeris',
                                           max_length=6, help_text='Iveskite automobilio valstybini numeri')
    automobilio_modelis_id = models.ForeignKey('Modelis', on_delete=models.SET_NULL, null=True)
    vin_kodas = models.CharField('VIN kodas', max_length=17, help_text='Iveskite VIN numeri')
    klientas = models.CharField('Klientas', max_length=100, help_text='Iveskite klienta')

    automobilis_pic = models.ImageField('Auto Nuotrauka', upload_to='car_pics', null=True, blank=True)

    aprasymas = HTMLField()

    def get_absolute_url(self):
        return reverse('auto-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = "Automobiliai"

    def __str__(self):
        return f'{self.valstybinis_numeris} /// {self.vin_kodas} /// {self.klientas}'


class Modelis(models.Model):
    marke = models.CharField('Automobilio marke', max_length=100, help_text='Iveskite automobilio marke')
    modelis = models.CharField('Automobilio modelis', max_length=100, help_text='Iveskite automobilio modeli')

    class Meta:
        verbose_name = "Modelis"
        verbose_name_plural = "Modeliai"

    def __str__(self):
        return f'{self.marke}, {self.modelis}'


class UzsakymasReview(models.Model):
    order_line = models.ForeignKey('UzsakymoEilute', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Atsiliepimas', max_length=2000)