from __future__ import unicode_literals
from django.utils.safestring import mark_safe
from django.db import models
from django.conf import settings

from multiselectfield import MultiSelectField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore import blocks

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block

    Special Thanks to Tim Allen
    https://github.com/FlipperPA/wagtail-components/
    """

    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
        ('json', 'JSON'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('yaml', 'YAML'),
        ('mysql', 'MySQL'),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )

        return mark_safe(highlight(src, lexer, formatter))

class CaosBlogPage(Page):
    """ Caos blog page admin controls """

    blog_head_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('caption', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('date', blocks.DateBlock()),
        ('codeblock', CodeBlock()),
    ])

    author = models.CharField(max_length=30, choices=getattr(settings, 'AUTHORS'))
    category = MultiSelectField(max_length=40, choices=getattr(settings, 'CATEGORIES'), max_choices=2, default=None)
    date = models.DateField("Post date")
    to_read = models.IntegerField("Length To Read", max_length=20)
    footer = RichTextField("Footnote", null=True, blank=True)
    disclaimer = RichTextField("Disclaimer", null=True, blank=True)

    indexed_fields = ('body',)
    search_name = "Caos Blog Page"