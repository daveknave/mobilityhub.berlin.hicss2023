from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel, StreamFieldPanel
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import (StreamField, RichTextField)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks

from wagtail.search import index

NEW_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'text',
    'autoColumnSize': False,
}



class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["flex.FlexPage", "services.Datensatz", "contact.ContactPage", "dataform.DataformPage"]
    max_count = 1
    
    lead_text = models.CharField(
        max_length=200, 
        blank=True, 
        help_text= "Subheading text under the banner title",
        )

    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text="Selcet an optional page to link to",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50,
        default="Read More",
        blank=False,
        help_text="Button Text",
    )

    banner_background_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The banner background image",
        on_delete=models.SET_NULL,
    )

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
       ("large_image", ImageChooserBlock(
            help_text='Das Bild wird auf 1200px by 775px zugeschnitten',
            template="streams/large_image_block.html"
        )),
       ("medium_image_text", blocks.MediumImageText()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html",
        )),
        ("pricing_table", blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS)),
    

        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            #features=["bold", "italic", "ol", "ul", "link"]
        )),
    
    ], null=True, blank=True)
    

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]

