# Generated by Django 3.2.9 on 2021-12-16 12:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('services', '0021_auto_20211213_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatenTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='services.datensatz')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_datentag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='services.DatenTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
