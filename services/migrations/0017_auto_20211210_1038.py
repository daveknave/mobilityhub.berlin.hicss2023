# Generated by Django 3.2.9 on 2021-12-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_auto_20211209_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datenkategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='Slug für die Kategorie der Daten', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Datenkategorie',
                'verbose_name_plural': 'Datenkategorien',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='datenquelle',
            options={'verbose_name': 'Datenquelle', 'verbose_name_plural': 'Datenquellen'},
        ),
    ]
