from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
    posts = Post.published.all()

    context = {
        "posts": posts,
    }

    return render(request, 'blog/post/list.xhtml', context)


def post_detail(request, year, month, day, post):
    try:
        # post = Post.published.get(id=id)
        post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    except Post.DoesNotExist:
        raise Http404("No Post found")

    context = {
        "post": post,
    }

    return render(request, 'blog/post/detail.xhtml', context)
