from wagtail.wagtailimages.models import Image

from blog.serializer import CaosBlogPageSerializer
from blog.models import CaosBlogPage

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

class BlogPageAPIView(viewsets.ModelViewSet):
    """ API view will return all live posts """

    queryset = CaosBlogPage.objects.live()
    serializer_class = CaosBlogPageSerializer

    @list_route()
    def live_blogs(self, request):
        """ 
        API list view will display all live posts and 
        pass additional image information
        """

        live_blogs = CaosBlogPage.objects.live()
        page = self.paginate_queryset(live_blogs)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(live_blogs, many=True)

        return Response(serializer.data)
