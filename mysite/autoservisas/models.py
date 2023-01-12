from django.db import models
from django.urls import reverse

# Create your models here.


class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200, help_text='Iveskite paslaugos pavadinima')
    kaina = models.CharField('Kaina', max_length=10, help_text='Iveskite paslaugos kaina')

    def __str__(self):
        return f'{self.pavadinimas} - {self.kaina}'


class UzsakymoEilute(models.Model):
    kiekis = models.CharField('Kiekis', max_length=2, help_text='Iveskite perkamos paslaugos kieki')
    kaina = 10
    paslauga_id = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    uzsakymas_id = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.uzsakymas_id} - {self.paslauga_id} - {self.kiekis} - {self.kaina}'


class Uzsakymas(models.Model):
    data = models.DateField('Uzsakymo data', null=True, blank=True)
    automobilis_id = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)
    suma = 10

    class Meta:
        ordering = ['data']

    def __str__(self):
        return f'{self.data} - {self.automobilis_id} - {self.suma}'


class Automobilis(models.Model):
    valstybinis_numeris = models.CharField('Automobilio valstybinis numeris',
                                           max_length=6, help_text='Iveskite automobilio valstybini numeri')
    automobilio_modelis_id = models.ForeignKey('Modelis', on_delete=models.SET_NULL, null=True)
    vin_kodas = models.CharField('VIN kodas', max_length=10, help_text='Iveskite VIN numeri')
    klientas = models.CharField('Klientas', max_length=100, help_text='Iveskite klienta')

    def __str__(self):
        return f'{self.valstybinis_numeris} - {self.vin_kodas} - {self.klientas}'


class Modelis(models.Model):
    marke = models.CharField('Automobilio marke', max_length=100, help_text='Iveskite automobilio marke')
    modelis = models.CharField('Automobilio modelis', max_length=100, help_text='Iveskite automobilio modeli')

    def __str__(self):
        return f'{self.marke}, {self.modelis}'

#
# class Genre(models.Model):
#     name = models.CharField('Pavadinimas', max_length=200, help_text='Iveskite knygos zanra')
#
#     def __str__(self):
#         return self.name
#
#
# class Book(models.Model):
#     title = models.CharField('Pavadinimas', max_length=200)
#     author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
#     summary = models.TextField('Aprasymas', max_length=1000, help_text='Trumpas knygos aprasymas')
#     isbn = models.CharField('ISBN', max_length=13)
#     # Rysys daug su daug
#     genre = models.ManyToManyField(Genre, help_text='Isrinkite zanra knygai')
#
#     def _str__(self):
#         return self.title
#
#     # Gauname linka
#     def absolute_url(self):
#         return reverse('book-detail', args=[str(self.id)])
#
#
# class BookInstance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus knygos kopijos ID')
#     book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#     due_back = models.DateField('Bus prieinama', null=True, blank=True)
#     LOAN_STATUS = (
#         ('a', 'Administruojama'),
#         ('p', 'Paimta'),
#         ('g', 'Galima paimti'),
#         ('r', 'Rezervuota')
#     )
#     status = models.CharField(
#         max_length=1,
#         choices=LOAN_STATUS,
#         blank=True,
#         default='a',
#         help_text='Status'
#     )
#
#     # nustatomas rykiavimas pagal (due back)
#     class Meta:
#         ordering = ['due_back']
#
#     def __str__(self):
#         return f'{self.id} {self.book.title}'
#
#
# class Author(models.Model):
#     first_name = models.CharField('Vardas', max_length=100)
#     last_name = models.CharField('Pavarde', max_length=100)
#
#     class Meta:
#         ordering = ['last_name', 'first_name']
#
#     def get_absolute_url(self):
#         return reverse('author-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return f'{self.last_name}, {self.first_name}'