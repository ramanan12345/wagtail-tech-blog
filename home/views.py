from django.shortcuts import render

from wagtail.wagtailsearch.models import Query

from blog.models import CaosBlogPage

def get_articles(request, search_type, search_for):
    """
    View will return search results based instant search
    or clicking a category and name. Results will return
    a paginated response.
    """

    template_name = "home/caos_home_page_search.html"
    unslug_search = search_for.replace('-', ' ')

    if 'category' in search_type:
        get_results = (CaosBlogPage.objects.live()
                       .search(unslug_search, fields=['category']))
        query = Query.get(unslug_search)
        query.add_hit()

    elif 'author' in search_type:
        get_results = (CaosBlogPage.objects.live()
                       .search(unslug_search, fields=['author']))
        query = Query.get(unslug_search)
        query.add_hit()

    else:
        get_results = CaosBlogPage.objects.none()

    context = {
        'search_results': get_results,
    }

    return render(request, template_name, context)
