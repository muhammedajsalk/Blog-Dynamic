from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from posts.models import Post,Category,Author


def index(request):
    posts = Post.objects.filter(is_deleted=False,is_draft=False)
    
    categories = Category.objects.all()[:5]
    authors = Author.objects.all()

    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)

    search_authors = request.GET.getlist("author")
    print(search_authors)
    if search_authors:
        posts =posts.filter(author__in = search_authors)
    
    search_categories = request.GET.getlist("category")
    print(search_categories)
    if search_categories:
        posts =posts.filter(categories__in = search_categories).distinct()

    instances = Paginator(posts, 3)
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