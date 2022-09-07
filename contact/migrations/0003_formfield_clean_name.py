# Generated by Django 3.2.9 on 2021-11-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20191208_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='clean_name',
            field=models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name'),
        ),
    ]
