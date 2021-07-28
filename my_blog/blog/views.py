from django.views import generic


from .models import Post, Category, Tag


class PostList(generic.ListView):
    queryset = Post.objects.all().select_related('author')
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class CategoryList(generic.ListView):
    queryset = Post.objects.all().select_related('author')
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(category__id=self.kwargs['pk'])
        return qs 

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering


class TagList(generic.ListView):
    queryset = Post.objects.all().select_related('author')
    template_name = 'post_list.html'

    def get_context_data(self, **kwargs):
        context = super(TagList, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(tags__id=self.kwargs['pk'])
        return qs 

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering
