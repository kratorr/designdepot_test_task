from django.urls import path

from .views import PostList, PostDetail, CategoryList, TagList

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    #path('blog/', PostList.as_view(), name='home'),
    path('post/<slug:pk>/', PostDetail.as_view(), name='post_detail'),
    path('category/<int:pk>/', CategoryList.as_view(), name='category'),
    path('tag/<int:pk>/', TagList.as_view(), name='tag')
]