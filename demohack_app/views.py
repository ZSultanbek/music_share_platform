from django.http import HttpResponse
from .models import Post
from django.shortcuts import render


def posts_list(request):

    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, '.templates/posts_list.html', context)
