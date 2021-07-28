from django.shortcuts import render


from django.utils import timezone
from django.views.generic.list import ListView

from .models import Post, Category, Tag


from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.all().select_related('author')
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        print(self.request.GET)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        qs = super(PostList, self).get_queryset()
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        if category:
            return qs.filter(category__name=category)
        elif tag:
            return qs.filter(tags__name=tag)
        else:
            return qs


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
