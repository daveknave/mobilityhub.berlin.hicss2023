from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from home.models import NEW_TABLE_OPTIONS
from streams import blocks

from wagtailcodeblock.blocks import CodeBlock 

class FlexPage(Page):
    parent_page_types = ["home.HomePage", "flex.FlexPage"]
    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html",
        )),
        ("pricing_table", blocks.PricingTableBlock(
            table_options=NEW_TABLE_OPTIONS,
        )),
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            #features=["bold", "italic", "ol", "ul", "link"]
        )),

        #("richtext_with_title", blocks.RichtTextWithTitleBlock()),


       ("richtext_code", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            features=["h2", "h3", "bold", "italic", "ol", "ul", "link", "code", "blockquote"]
        )),

        ("code", CodeBlock(label='Code')),


        ("large_image", ImageChooserBlock(
            help_text='Das Bild wird auf 1200px by 775px zugeschnitten',
            template="streams/large_image_block.html"
        )),
        ("medium_image_text", blocks.MediumImageText()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flex (misc) page"
        verbose_name_plural = "Flex (misc) pages"