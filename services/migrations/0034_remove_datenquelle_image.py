# Generated by Django 3.2.9 on 2022-01-13 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0033_auto_20220113_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datenquelle',
            name='image',
        ),
    ]
