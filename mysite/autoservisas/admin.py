from django.contrib import admin
from .models import Paslauga, UzsakymoEilute, Uzsakymas, Automobilis, Modelis


class UzsakymoEiluteInline(admin.TabularInline):
    model = UzsakymoEilute
    extra = 0
    readonly_fields = ('id',)


class UzsakymasAdmin(admin.ModelAdmin):
    inlines = [UzsakymoEiluteInline]
    list_display = ('data', 'automobilis_id')


class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')


class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_modelis_id', 'valstybinis_numeris', 'vin_kodas')
    search_fields = ('klientas', 'automobilio_modelis_id__marke', 'automobilio_modelis_id__modelis', 'vin_kodas',
                     'valstybinis_numeris')
    list_filter = ('klientas', 'automobilio_modelis_id__marke', 'automobilio_modelis_id__modelis')


class ModelisAdmin(admin.ModelAdmin):
    list_display = ('marke', 'modelis')


class UzsakymoEiluteAdmin(admin.ModelAdmin):
    # inlines = [UzsakymasInline]
    list_display = ('kiekis', 'kaina', 'paslauga_id', 'uzsakymas_id')


# Register your models here.
admin.site.register(Paslauga, PaslaugaAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(UzsakymoEilute, UzsakymoEiluteAdmin)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Modelis, ModelisAdmin)
