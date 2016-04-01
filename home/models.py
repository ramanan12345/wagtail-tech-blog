from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page

from blog.models import CaosBlogPage

class CaosHomePage(Page):
    """ Caos home page admin controls """

    indexed_fields = ('body',)
    search_name = "TechBlog Home Page"

    @property
    def blogs(self):
        """
        Property will return all live blogs ordered
        by their ID or creation date
        """

        blogs = CaosBlogPage.objects.live().descendant_of(self)
        blogs = blogs.order_by('-id')

        return blogs

    def get_context(self, request, tag=None):
        """
        Simple paginator that will take the results from
        property blogs and return the results as a paginated
        response to our template
        """

        blogs = self.blogs
        page = request.GET.get('page')
        paginator = Paginator(blogs, getattr(settings, 'MAX_PAGINATION', 4))

        try:
            blogs = paginator.page(page)

        except PageNotAnInteger:
            blogs = paginator.page(1)

        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(CaosHomePage, self).get_context(request)
        context['blogs'] = blogs

        return context
