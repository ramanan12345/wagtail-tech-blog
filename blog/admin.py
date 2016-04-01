from django.conf import settings
from django import forms

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from blog.models import CaosBlogPage

# CaosBlogPage page admin panels
CaosBlogPage.content_panels = [
    ImageChooserPanel('blog_head_img'),
    FieldPanel('title', classname='full title'),
    FieldPanel('date'),
    FieldPanel('to_read'),
    FieldRowPanel([
        FieldPanel('author', classname="col6"),
        FieldPanel('category', classname="col6", 
            widget=forms.SelectMultiple(choices=getattr(settings, 'CATEGORIES'))),
    ], classname="full"),
    StreamFieldPanel('body'),
    FieldPanel('footer'),
    FieldPanel('disclaimer'),
]
