# Generated by Django 3.2.9 on 2022-01-29 13:41

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0009_alter_flexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text1', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text2', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('text3', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automagically cropped 570px by 370px')), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])))])), ('image_and_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image the automagically cropped to 786px by 552px')), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on the left with text on the right. Or image on the right with text on the left.')), ('title', wagtail.core.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Max length of 200 characters.', max_length=200)), ('link', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='', max_length=50, required=False)), ('internal_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False))]))])), ('testimonial', wagtail.snippets.blocks.SnippetChooserBlock(target_model='testimonials.Testimonial', template='streams/testimonial_block.html')), ('pricing_table', streams.blocks.PricingTableBlock(table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': ['row_above', 'row_below', '---------', 'col_left', 'col_right', '---------', 'remove_row', 'remove_col', '---------', 'undo', 'redo'], 'editor': 'text', 'minSpareRows': 0, 'renderer': 'text', 'rowHeaders': True, 'startCols': 4, 'startRows': 4, 'stretchH': 'all'})), ('richtext', wagtail.core.blocks.RichTextBlock(template='streams/simple_richtext_block.html')), ('richtext_code', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'link', 'code', 'blockquote'], template='streams/simple_richtext_block.html')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code')), ('large_image', wagtail.images.blocks.ImageChooserBlock(help_text='Das Bild wird auf 1200px by 775px zugeschnitten', template='streams/large_image_block.html')), ('medium_image_text', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=300, required=False))]))], blank=True, null=True),
        ),
    ]
