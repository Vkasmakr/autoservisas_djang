# Generated by Django 4.1.1 on 2023-01-23 09:54

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0006_automobilis_aprasymas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilis',
            name='aprasymas',
            field=tinymce.models.HTMLField(),
        ),
    ]
