from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query

from django.conf import settings

def search(request):
    """ Simple Admin and Search Feature """

    template_name = 'search/search.html'
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)
        query.add_hit()

    else:
        search_results = Page.objects.none()

    paginator = (Paginator(search_results, 
        getattr(settings, 'MAX_PAGINATION_SEARCH', 10)))

    try:
        search_results = paginator.page(page)

    except PageNotAnInteger:
        search_results = paginator.page(1)

    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    context = {'search_query': search_query, 'search_results': search_results}

    return render(request, template_name, context)
