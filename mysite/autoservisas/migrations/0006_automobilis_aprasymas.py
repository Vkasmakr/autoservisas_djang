# Generated by Django 4.1.1 on 2023-01-23 09:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0005_uzsakymoeilute_grazinti_iki_uzsakymoeilute_useris'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilis',
            name='aprasymas',
            field=tinymce.models.HTMLField(default='Aprasymas'),
        ),
    ]
