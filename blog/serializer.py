from wagtail.wagtailimages.models import Image
from rest_framework import serializers

from blog.models import CaosBlogPage

import socket

class CaosBlogPageSerializer(serializers.ModelSerializer):
    """ CaosBlog page serializer """

    img_url = serializers.SerializerMethodField()

    class Meta:
        model = CaosBlogPage
        fields = ('date', 'author', 'category', 'img_url', 'url',)

    def get_img_url(self, obj):
        """ Helper method will return a url for image """

        img = Image.objects.get(id=obj.blog_head_img_id)
        img_url = img.get_rendition('fill-320x200')

        if 'apps' in socket.gethostname():
            return img_url.url
        else:
            build_url = "https://%s%s" % (socket.gethostname(), img_url.url)
            return build_url 
