from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('blog/', PostList.as_view(), name='home'),
    path('post/<slug:pk>/', PostDetail.as_view(), name='post_detail'),
]