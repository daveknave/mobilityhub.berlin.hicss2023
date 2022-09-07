from django.db import models
from django.core.exceptions import ValidationError
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    PageChooserPanel, 
    StreamFieldPanel, 
    MultiFieldPanel, 
    InlinePanel)
from modelcluster.fields import ParentalKey
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import (StreamField, RichTextField)
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from streams import blocks
from wagtail.search import index
from django import forms
import datetime
from modelcluster.fields import ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from taggit.models import Tag as TaggitTag
from django_extensions.db.fields import AutoSlugField
import pandas as pd


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

@register_snippet
class Datenquelle(models.Model):
    """DatenQuelle für snippets."""

    name = models.CharField(max_length=100)
    website = models.URLField(
        blank=True,
        max_length=200,
        null=True,
        )
    ansprech = models.CharField(
        blank=True,
        max_length=200,
        null=True,
        )
    adresse = models.CharField(
        blank=True,
        max_length=200,
        null=True,
        )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        )
    


    panels = [
            MultiFieldPanel(
                [
                    FieldPanel("name"),
                ],
                heading="Name",
            ),
            MultiFieldPanel(
                [
                    FieldPanel("website"),
                    ImageChooserPanel("image")
                ],
                heading="Bild und Webseite"
            ),
            MultiFieldPanel(
                [
                    FieldPanel("adresse"),
                    FieldPanel("ansprech")
                ],
                heading="Kontakt"
            )
    ]

    def __str__(self):
            """String repr of this class."""
            return self.name

    class Meta:  # noqa
        verbose_name = "Datenquelle"
        verbose_name_plural = "Datenquellen"

#register_snippet(Datenquelle)



class DatenQuelleOrderable(Orderable):
    page = ParentalKey("services.Datensatz", related_name="datenquelle")
    datenquelle = models.ForeignKey(
        "services.Datenquelle",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("datenquelle"),
    ]


@register_snippet
class Datenkategorie(models.Model):
#slug für url !!!
    name = models.CharField(max_length=255)
    slug = AutoSlugField(
        populate_from=['name'],
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
    )

    panels = [
        FieldPanel("name"),
        #FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Datenkategorie"
        verbose_name_plural = "Datenkategorien"
        ordering = ["name"]

    def __str__(self):
        return self.name


class DatenTag(TaggedItemBase):
    content_object = ParentalKey(
        'Datensatz',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True

class PostPageTag(TaggedItemBase):
    content_object = ParentalKey("Datensatz", related_name="data_tags")


class GeometrieAuswahl(models.TextChoices):
    Ja = 'J', ('Ja')
    Nein = 'N', ('Nein')



class Datensatzübersicht(Page):
    parent_page_types = ["home.Homepage"]
    subpage_types = ["services.Datensatz"]
    max_count = 1

    template = "services/datensatzübersicht.html"
    subtitle = models.TextField(
        blank=True,
        max_length=500,

    )
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    def get_child_tags(self):
        tags = []
        news_pages = Datensatz.objects.live().public();
        for page in news_pages:
            # Not tags.append() because we don't want a list of lists
            tags += page.tags.all()
        tags = sorted(set(tags))
        return tags
  
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = Datensatz.objects.live().public()
        context['Datenquelle'] = Datenquelle.objects.all()
        
        
        context['Datenkategorie'] = Datenkategorie.objects.all()
        context['Tags'] = self.get_child_tags()
        context['services_filter'] = Datensatz.objects.live().public().filter(Datenkategorie__slug__in=[request.GET.get('category')])
        
        posts = Datensatz.objects.live().public()
        context["recent_posts"] = posts[:5]
        category_slug = request.GET.get("category", None)
        context["blog_posts"] = posts
        if category_slug:
            if posts.filter(Datenkategorie__slug__contains=category_slug).count() > 0:
                context["blog_posts"] = posts.filter(Datenkategorie__slug__contains=category_slug)
            else:
                context["blog_posts"] = posts  
        
        all_posts = Datensatz.objects.live().public()
        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_posts = all_posts.filter(tags__slug__in=[tags])
        context["posts"] = all_posts



        posts = Datensatz.objects.live().public()

        category_slug = request.GET.get("category", None)
        tag_slug = request.GET.get('tag', None)
        context["blog_posts"] = posts
        tags = request.GET.get('tag')
        

        if category_slug:
            if posts.filter(Datenkategorie__slug__contains=category_slug).count() > 0:
                context["blog_posts"] = posts.filter(Datenkategorie__slug__contains=category_slug)
            else:
                context["blog_posts"] = posts  
        
        elif tag_slug:
            context["blog_posts"] = posts.filter(tags__slug__in=[tags])
            
        return context




class Datensatz(Page):
    parent_page_types = ["services.Datensatzübersicht"]
    subpage_types = []
    template = "services/datensatz.html"

    untertitel = models.TextField(
        blank=False,
        max_length=400,
        help_text="Bitte beschreiben Sie den Datensatz in 400 Zeichen",
    )

    Beschreibung = models.TextField(
        blank=False,
        max_length=4000,
        help_text="Bitte beschreiben Sie den Datensatz ausführlich",
        null=True,
    )

    datensatz_extern = models.URLField(blank=True)
    
    datensatz_referenz = models.URLField(blank=True)

    #button_text = models.CharField(blank=True, max_length=50)

    datensatz_bild = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text="",
        related_name="+",
    )

    datensatz_intern = models.ForeignKey(
            'wagtaildocs.Document',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )


    ort = models.TextField(
        blank=True,
        max_length=100,
        null=True,
        help_text="Ort bzw. Region, in der die Daten erhoben wurden",
        
    )

    anfangsdatum = models.DateField(("Anfangsdatun"), blank=True)

    enddatum = models.DateField(("Enddatum"), blank=True)

    datum_angepasst = models.DateField(("Zuletzt angepasst"), help_text="Wann wurden die Daten das letzte mal angepasst?", blank=True,)

    datumhochgeladen = models.DateField(("Hochgeladen am"), default=datetime.date.today, blank=True, help_text="Wann wurden die Daten hochgeladen",)


    geometrie = models.TextField(
        blank=True,
        max_length=200,
        null=True,
    )

    groesse_datensatz = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Wie groß ist die Datei bzw. die Dateien des Datensatzes?",
    )

    dateiformat = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Welches Dateiformat hat der Datensatz? Z.B.: CSV, XLSX,...",
    )

    anzahl_an_dateien = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Wieviele Dateien wurden hochgeladen?",
    )

    version_des_datensatzes = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="In welcher Version befindet sich der Datensatz? Z.B.: V1",
    )

    lizens_des_datensatzes = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Wie ist der Datensatz nutzbar und gibt es eine Lizens für die Daten?",
    )

    links = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Gibt es weiterführende Links?",
    )

    branche = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Innerhalb welcher Branche wurden die Daten erfasst?",
    )

    update_zyklus = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="In welchem Zyklus werden die Daten vorrausichtlich aktualisiert?",
    )

    publiziert_in = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="Wurden die Daten bereits veröffentlicht? Wenn ja, in welchem Journal / auf welcher Konferenz?",
    )


    button = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        related_name="+",
        help_text="Bitte die Seite 'Datenübersicht' auswählen",
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50,
        default="Datensatzübersicht",
        blank=False,
        help_text="Datensatzübersicht Button",
    )

    versions_hist = models.URLField(
        blank=True,
        )

    version_des_datensatzes_alt = models.TextField(
        blank=True,
        max_length=400,
        null=True,
        help_text="In welcher Version befindet sich die letzte Version des Datensatez? Z.B.: V1.0",
    )
    #df = pd.read_csv(self.datensatz_intern.url)
   # df = pd.read_csv("rocketman/static/csv/test.csv")
  
    # parsing the DataFrame in json format.
    #meinepandastable = df.to_html()

    #from django.http import HttpRequest
    #request = HttpRequest()

    #meinepandastable = pv.Table(request) 
    

    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("richtext", wagtail_blocks.RichTextBlock(
            template="streams/simple_richtext_block.html",
            #features=["bold", "italic", "ol", "ul", "link"]
        )),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html",
        )),
        ("large_image", ImageChooserBlock(
            help_text='Das Bild wird auf 1200px by 775px zugeschnitten',
            template="streams/large_image_block.html"
        )),
        ("medium_image_text", blocks.MediumImageText()),
        ("pricing_table", blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS)),
    
    ], null=True, blank=True)

    

    Datenkategorie = ParentalManyToManyField("services.Datenkategorie", blank=False)

    #tags = ClusterTaggableManager(through=DatenTag, blank=True)

    tags = ClusterTaggableManager(through="services.PostPageTag", blank=False, help_text="Durch Kommas getrennte Tags ",)


    content_panels = Page.content_panels + [
        FieldPanel("untertitel"),
        FieldPanel("Beschreibung"),
        ImageChooserPanel("datensatz_bild"),
        MultiFieldPanel(
            [
                FieldPanel("Datenkategorie", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Datenkategorie"
        ),
        FieldPanel("tags"),
        MultiFieldPanel(
            [
                InlinePanel("datenquelle", label="Datenquelle", min_num=0, max_num=10)
            ],
            heading="Datenquelle bzw. Author *"
        ),
        FieldPanel("groesse_datensatz"),
        FieldPanel("dateiformat"),
        FieldPanel("anzahl_an_dateien"),
        FieldPanel("datumhochgeladen"),
        FieldPanel("datum_angepasst"),
        FieldPanel("version_des_datensatzes"),
        FieldPanel("version_des_datensatzes_alt"),
        FieldPanel("versions_hist"),
        FieldPanel("lizens_des_datensatzes"),
        FieldPanel("anfangsdatum"),
        FieldPanel("enddatum"),
        FieldPanel("ort"),
        FieldPanel("geometrie"),
        FieldPanel("links"),
        FieldPanel("branche"),
        FieldPanel("update_zyklus"),
        FieldPanel("publiziert_in"),
        DocumentChooserPanel('datensatz_intern'),
        FieldPanel("datensatz_extern"),
        FieldPanel("datensatz_referenz"),
        StreamFieldPanel("body"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
    ]

    def clean(self):
            super().clean()

            if self.datensatz_intern and self.datensatz_extern and self.datensatz_referenz:
                # alle drei felder ausgefüllt
                raise ValidationError({
                    'datensatz_intern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_extern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_referenz': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                })

            if not self.datensatz_intern and not self.datensatz_extern and not self.datensatz_referenz:
            # alle drei felder leer
                raise ValidationError({
                    'datensatz_intern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_extern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_referenz': ValidationError("YBitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                })

            if  self.datensatz_intern and  self.datensatz_extern and not self.datensatz_referenz:
            # datensatz intern + datensatz extern ausgefüllt
                raise ValidationError({
                    'datensatz_intern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_extern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_referenz': ValidationError("YBitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                })
            

            if  self.datensatz_intern and not self.datensatz_extern and  self.datensatz_referenz:
            # datensatz intern + datensatz referenz ausgefüllt
                raise ValidationError({
                    'datensatz_intern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_extern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_referenz': ValidationError("YBitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                })

            if not self.datensatz_intern and  self.datensatz_extern and  self.datensatz_referenz:
            # datensatz extern + datensatz referenz ausgefüllt
                 raise ValidationError({
                    'datensatz_intern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_extern': ValidationError("Bitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                    'datensatz_referenz': ValidationError("YBitte wähle einen internen Datensatz, fülle das Feld für eine externen Datensatz oder eine Datensatz Referenz aus."),
                })



                #datensatz_intern
                #datensatz_extern
                #datensatz_referenz



            #datasetIntern = datensatz_intern.objects.values()
            #datasetIntern = datensatz_intern.objects.()
            #datasetIntern = datensatz_intern.objects.all()
            #datasetIntern = datensatz_intern_url()
            #datasetIntern = datensatz_intern_url.objects.all()
            #datasetIntern = self.datensatz_intern_url()
            #datasetIntern = self.datensatz_intern_url.objects()
            #datasetIntern = self.datensatz_intern_url.objects.all()


            #datasetInternPandas = pd.Dataframe(datasetIntern)

            #datasetInternHTML = pd.datasetInternPandas.to_html()




