from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from posts.models import Post,Category,Author


def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)
    
    categories = Category.objects.all()
    authors = Author.objects.all()

    search_authors = request.GET.getlist("author")
    print(search_authors)
    if search_authors:
        posts =posts.filter(author__in = search_authors)

    instances = Paginator(posts, 2)
    page = request.GET.get('page', 1)

    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)


    context={
        "title" : "Home Page",
        "instances" : instances,
        "categories" : categories,
        "authors" : authors
    }
    return render(request, 'web/index.html',context=context)