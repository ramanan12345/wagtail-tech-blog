from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from about.models import CaosAboutPage

# CaosAboutPage Admin Panels
CaosAboutPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    ImageChooserPanel('about_head_img'),
]
