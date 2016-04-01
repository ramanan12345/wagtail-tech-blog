from django import template
from about.models import Profile

register = template.Library()

@register.inclusion_tag('snippet_profiles.html', takes_context=True)
def profiles(context):
    """ Tag will return all users that exist in model Profiles """

    return {
        'Profiles': Profile.objects.all(),
        'request': context['request'],
    }
