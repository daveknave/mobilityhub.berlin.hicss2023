from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField


@register_setting
class TextFooter(BaseSetting):

    contact = RichTextField(
        blank=True,
        null=True,
        features=["link"],
    )

    panels = [
        FieldPanel("contact")
    ]


@register_setting
class PartnerLinks(BaseSetting):

    hours = RichTextField(
        blank=True,
        null=True,
        features=[],
    )

    panels = [
        FieldPanel("hours")
    ]



@register_setting
class SocialMediaLinks(BaseSetting):

    facebook = models.URLField(
        blank=True,
        help_text='Enter your Facebook URL'
    )
    twitter = models.URLField(
        blank=True,
        help_text='Enter your Twitter URL'
    )
    youtube = models.URLField(
        blank=True,
        help_text='Enter your YouTube URL'
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter your Instagram URL'
    )
    linkedin = models.URLField(
        blank=True,
        help_text='Enter your LinkedIn URL'
    )

    panels = [
        FieldPanel("facebook"),
        FieldPanel("twitter"),
        FieldPanel("youtube"),
        FieldPanel("instagram"),
        FieldPanel("linkedin"),
    ]

 

@register_setting
class FooterCTASettings(BaseSetting):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=25, default='Contact Us')
    button_internal_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='If an internal page is selected, it will be used before the external page.'
    )
    button_external_page = models.URLField(blank=True, help_text='If an internal page is selected, it will be used before the external page.')

    panels = [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("button_text"),
        PageChooserPanel("button_internal_page"),
        FieldPanel("button_external_page"),
    ]
