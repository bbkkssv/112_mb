from django.urls import path
from .views import PostCreateView, PostDeleteView, PostListView, PostDetailView,PostUpdateView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    ]