from django.shortcuts import render
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'blog/blog_list.html'
# Create your views here.
