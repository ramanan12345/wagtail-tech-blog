from django.contrib.syndication.views import Feed
from django.conf import settings

from blog.models import CaosBlogPage

import re

class NewestPosts(Feed):
    """ RSS feed will return the top most recent articles """

    title = getattr(settings, 'NEWEST_BLOG_TITLE', 'TechBlog')
    link = '/latest/'
    description = getattr(settings, 'NEWEST_BLOG_DESCRIPTION', '...')

    def items(self):
        return (CaosBlogPage.objects.live()
                .order_by('-date')[:getattr(settings, 'NEWEST_BLOG_FEED_LENGTH', 5)])

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        content = ''
        for streamfield in item.body:
            if 'caption' in streamfield.block_type:
                content = (streamfield.value.source
                        .replace('<p>', '').replace('</p>', ''))
                break
        desc = re.compile(r'<.*?>').sub('', content)
        if len(desc) > 250:
            desc = desc[:250] + '...'

        return desc

    def item_link(self, item):
        return item.url
