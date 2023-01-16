# Generated by Django 4.1.1 on 2023-01-16 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0002_uzsakymas_suma_uzsakymoeilute_kaina_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='modelis',
            options={'verbose_name': 'Modelis', 'verbose_name_plural': 'Modeliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'ordering': ['data'], 'verbose_name': 'Uzsakymas', 'verbose_name_plural': 'Uzsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymoeilute',
            options={'verbose_name': 'Uzsakymo eilute', 'verbose_name_plural': 'Uzsakymo eilutes'},
        ),
        migrations.AddField(
            model_name='uzsakymas',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Uzsakymas gautas'), ('p', 'Uzsakymas priimtas'), ('g', 'Uzsakymas vykdomas'), ('r', 'Uzsakymas baigtas')], default='a', help_text='Status', max_length=1),
        ),
    ]