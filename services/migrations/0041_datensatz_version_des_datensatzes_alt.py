# Generated by Django 3.2.9 on 2022-02-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0040_auto_20220204_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='datensatz',
            name='version_des_datensatzes_alt',
            field=models.TextField(blank=True, help_text='In welcher Version befindet sich die letzte Version des Datensatez? Z.B.: V1.0', max_length=400, null=True),
        ),
    ]
