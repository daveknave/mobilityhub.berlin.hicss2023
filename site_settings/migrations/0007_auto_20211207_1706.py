# Generated by Django 3.2.9 on 2021-12-07 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('site_settings', '0006_socialmediasettings_linkedin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HoursSettings',
            new_name='FördererSettings',
        ),
        migrations.RenameField(
            model_name='förderersettings',
            old_name='hours',
            new_name='förderer',
        ),
    ]
