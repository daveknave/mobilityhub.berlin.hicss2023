# Generated by Django 3.2.9 on 2021-12-08 10:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('services', '0009_auto_20211207_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datensatz',
            name='anfangsdatum',
            field=models.DateField(default=datetime.date.today, verbose_name='Anfangsdatun'),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('richtext', wagtail.core.blocks.RichTextBlock(template='streams/simple_richtext_block.html')), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped 570px by 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image the automagically cropped to 786px by 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the right. Or image on the right with text on the left.')), ('title', wagtail.core.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 characters.', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='More Details', max_length=50)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'}))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='datensatz_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='enddatum',
            field=models.DateField(default=datetime.date.today, verbose_name='Enddatum'),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='geometrie',
            field=models.TextField(choices=[('J', 'Ja'), ('N', 'Nein')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='datensatz',
            name='quelle',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
