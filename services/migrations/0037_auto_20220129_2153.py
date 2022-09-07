# Generated by Django 3.2.9 on 2022-01-29 21:53

import datetime
from django.db import migrations, models
import modelcluster.contrib.taggit
import modelcluster.fields
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('services', '0036_alter_datensatz_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datensatz',
            old_name='geometrie1',
            new_name='groesse',
        ),
        migrations.RenameField(
            model_name='datensatz',
            old_name='description',
            new_name='untertitel',
        ),
        migrations.RemoveField(
            model_name='datensatz',
            name='datum',
        ),
        migrations.RemoveField(
            model_name='datensatz',
            name='quelle',
        ),
        migrations.AddField(
            model_name='datensatz',
            name='aktuelldatum',
            field=models.DateField(default=datetime.date.today, verbose_name='Zuletzt angepasst'),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='anzahl',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='branche',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='dateiformat',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='links',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='lizens',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='publiziert',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='updates',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='datensatz',
            name='version',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='Datenkategorie',
            field=modelcluster.fields.ParentalManyToManyField(to='services.Datenkategorie'),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('richtext', wagtail.core.blocks.RichTextBlock(template='streams/simple_richtext_block.html')), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text1', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text2', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text3', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped 570px by 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image the automagically cropped to 786px by 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the right. Or image on the right with text on the left.')), ('title', wagtail.core.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 characters.', max_length=200, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='Das Bild wird auf 1200px by 775px zugeschnitten', template='streams/large_image_block.html')), ('medium_image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=300, required=False))])), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'}))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='geometrie',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='ort',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(help_text='A comma-separated list of tags.', through='services.PostPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
