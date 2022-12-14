from django.shortcuts import render
from .models import Post, Tag
from django.http import Http404



def PostListView(request):
  posts = Post.objects.all().order_by('-id')
  
  context = {
    'posts': posts,
  }
  return render(request, 'posts/list.html', context)


def PostDetailView(request, slug=None):
  if slug is not None:
    try: 
      post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
      raise Http404
  context = {
    'post': post,
  }
  return render(request, 'posts/detail.html', context)

def page_not_found(request, exception):
  return render(request, '404.html')