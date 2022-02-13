from django.urls import path
from .views import PostListView,PostCreateView, PostUpdateView,PostDeleteView, post_detail, add_comment
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:id>/',post_detail, name='post-detail'),
    path('post/<int:id>/comment/',add_comment, name='add-comment'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]