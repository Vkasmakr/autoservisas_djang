from django.contrib import admin
from .models import Paslauga, UzsakymoEilute, Uzsakymas, Automobilis, Modelis

# Register your models here.
admin.site.register(Paslauga)
admin.site.register(Uzsakymas)
admin.site.register(UzsakymoEilute)
admin.site.register(Automobilis)
admin.site.register(Modelis)
