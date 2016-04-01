from wagtail.wagtailadmin.edit_handlers import FieldPanel

from home.models import CaosHomePage

# CaosHomePage admin panels
CaosHomePage.content_panels = [
    FieldPanel('title', classname="full title"),
]
