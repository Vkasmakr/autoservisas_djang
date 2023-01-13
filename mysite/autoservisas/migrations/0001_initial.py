# Generated by Django 4.1.1 on 2023-01-12 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valstybinis_numeris', models.CharField(help_text='Iveskite automobilio valstybini numeri', max_length=6, verbose_name='Automobilio valstybinis numeris')),
                ('vin_kodas', models.CharField(help_text='Iveskite VIN numeri', max_length=10, verbose_name='VIN kodas')),
                ('klientas', models.CharField(help_text='Iveskite klienta', max_length=100, verbose_name='Klientas')),
            ],
        ),
        migrations.CreateModel(
            name='Modelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marke', models.CharField(help_text='Iveskite automobilio marke', max_length=100, verbose_name='Automobilio marke')),
                ('modelis', models.CharField(help_text='Iveskite automobilio modeli', max_length=100, verbose_name='Automobilio modelis')),
            ],
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pavadinimas', models.CharField(help_text='Iveskite paslaugos pavadinima', max_length=200, verbose_name='Pavadinimas')),
                ('kaina', models.CharField(help_text='Iveskite paslaugos kaina', max_length=10, verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Uzsakymo data')),
                ('automobilis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.automobilis')),
            ],
            options={
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiekis', models.CharField(help_text='Iveskite perkamos paslaugos kieki', max_length=2, verbose_name='Kiekis')),
                ('paslauga_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.paslauga')),
                ('uzsakymas_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.uzsakymas')),
            ],
        ),
        migrations.AddField(
            model_name='automobilis',
            name='automobilio_modelis_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.modelis'),
        ),
    ]