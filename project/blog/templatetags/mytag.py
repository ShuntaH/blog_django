import os
from django import template

register = template.Library()

"""
このfileをsettings.pyのinstalled appに登録
"""


@register.simple_tag()
def url_replace(request, field, value):
    """Get pramを一部書き換える"""
    url_dict = request.GET.copy()
    url_dict[field] = value
    return url_dict.urlencode()


@register.filter
def get_filename(value):
    """
    Return the name of file
    """
    return os.path.basename(value.file.name)
