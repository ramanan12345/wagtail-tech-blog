from django.test import TestCase

from wagtail.wagtailcore.models import Page, Site

from home.models import CaosHomePage
from blog.models import CaosBlogPage

from unittest.mock import Mock
from datetime import datetime as Date

class MyPageTests(TestCase):

    def setUp(self):
        home_page = CaosHomePage(title='TestHomePage')
        root_page = Page.get_root_nodes()[0]
        root_page.add_child(instance=home_page)
        sites = Site.objects.get(id=1)
        sites.root_page = home_page
        sites.save()

    def create_blog_posts(self, title, *args):
        """ Helper to populate our homepage with blog posts """

        settings = args[0] if args else {}
        blog_post = CaosBlogPage(
            title=title,
            author= settings.get('author', 'Test Author'),
            category= settings.get('category', ['Python',]),
            date = settings.get('date', Date.now()),
            to_read = settings.get('to_read', 20),
            search_description='',
            seo_title='foo',
            show_in_menus=False,
            slug = settings.get('slug', 'randomslug')
        )

        home_page = CaosHomePage.objects.all()[0]
        blog_post.body.steam_data = [('caption', 'This Post')]
        home_page.add_child(instance=blog_post)

    def test_CaosHomePage__pagination_no_posts_to_paginate(self):
        """ Test Case - No blogs are available so no pagination """

        request = Mock()
        home_page = CaosHomePage.objects.all()[0]
        response = home_page.get_context(request)

        request.GET.get.assert_called_once_with('page')
        self.assertFalse(response['blogs'].has_next())

    def test_CaosHomePage__pagination_with_5_posts(self):
        """ Test Case - Pagination should occur as there are 5 posts """

        home_page = CaosHomePage.objects.all()[0]
        request = Mock()
        blog_settings = [
            ('blogpost1', {'slug': 'slug1'}),
            ('blogpost2', {'slug': 'slug2'}),
            ('blogpost3', {'slug': 'slug3'}),
            ('blogpost4', {'slug': 'slug4'}),
            ('blogpost5', {'slug': 'slug5'}),
        ]

        for title, slug in blog_settings:
            self.create_blog_posts(title, slug)

        response = home_page.get_context(request)

        request.GET.get.assert_called_once_with('page')
        self.assertTrue(response['blogs'].has_next())
        self.assertTrue(response['blogs'].paginator._num_pages == 2)

    def test_CaosHomePage__property_blogs_returns_live_blogs_correctly(self):
        """ Test Case - property will return blogs in order based on ID """

        home_page = CaosHomePage.objects.all()[0]
        for title in range(3):
            posts = 'posts' + str(title)
            self.create_blog_posts(posts)

        self.assertTrue(list((blog.id for blog in CaosBlogPage.objects.live().order_by('-id')))
                == list((live_posts.id for live_posts in home_page.blogs)))
        self.assertTrue(len(home_page.blogs) > 0)
