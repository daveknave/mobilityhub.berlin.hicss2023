# Generated by Django 3.2.9 on 2021-12-07 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('site_settings', '0007_auto_20211207_1706'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FördererSettings',
            new_name='HoursSettings',
        ),
        migrations.RenameField(
            model_name='hourssettings',
            old_name='förderer',
            new_name='hours',
        ),
    ]
