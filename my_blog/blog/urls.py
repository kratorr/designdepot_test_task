from django.urls import path

from .views import PostList, PostDetail, CategoryList, TagList
from .views import FeedbackCreateView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:pk>/', PostDetail.as_view(), name='post_detail'),
    path('category/<int:pk>/', CategoryList.as_view(), name='category'),
    path('tag/<int:pk>/', TagList.as_view(), name='tag'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback')
]
