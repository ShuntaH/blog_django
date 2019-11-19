from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Post, Category


# Create your views here.


class IndexView(generic.ListView):
    model = Post  # make html file name as model name + list.html
    paginate_by = 7

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')  # 新しい投稿順
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)

            )
        return queryset


class CategoryView(generic.ListView):
    model = Post
    paginate_by = 7

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.all().order_by('-created_at')
        queryset = queryset.filter(category=category)
        return queryset


class DetailView(generic.DetailView):
    model = Post
