from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
  path('', PostListView, name='list-view'),
  path('<slug:slug>/', PostDetailView, name='detail-view'),
]