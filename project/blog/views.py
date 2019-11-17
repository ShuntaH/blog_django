from django.shortcuts import render
from django.views import generic

from .models import Post
# Create your views here.


class IndexView(generic.ListView):
    model = Post  # make html file name as model name + list.html

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')  # 新しい投稿順
