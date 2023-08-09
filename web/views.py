from django.shortcuts import render
from django.http.response import HttpResponse
from posts.models import Post


def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)
    context={
        "title" : "Home Page",
        "posts" : posts
    }
    return render(request, 'web/index.html',context=context)