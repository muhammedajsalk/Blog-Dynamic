from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from posts.models import Post


def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)
    
    instances = Paginator(posts, 6)
    page = request.GET.get('page', 1)

    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)


    context={
        "title" : "Home Page",
        "instances" : instances
    }
    return render(request, 'web/index.html',context=context)