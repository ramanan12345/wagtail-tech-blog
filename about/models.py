from __future__ import unicode_literals
from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.models import Page, Orderable
from modelcluster.fields import ParentalKey


@register_snippet
class Profile(models.Model):
    """
    Snippet will allow the editor to add/remove team
    members via admin tool and content will dynamically
    display.
    """

    profile_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)

    panels = [
        ImageChooserPanel('profile_img'),
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('bio'),
    ]

    def __str__(self):
        return self.name

class ProfileIndex(Orderable, models.Model):
    """ Setting our model relations to our Profiles Snippet """

    page = ParentalKey('CaosAboutPage', related_name='CaosProfiles')
    profile = models.ForeignKey('Profile', related_name='+')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    panels = [
        SnippetChooserPanel('profile', Profile),
    ]

class CaosAboutPage(Page):
    """ Caos about page admin controls """

    about_head_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    date = models.DateField("Date")
