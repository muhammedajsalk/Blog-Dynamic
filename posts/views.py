import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm
from posts.models import Author


@login_required(login_url="/users/login/")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            if not Author.objects.filter(user=request.user).exists():
                author = Author.objects.create(user=request.user,name=request.user.username)
            else:
                author = request.user.author
            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.author = author
            instance.save()
    else:
        data = {
            "title": "Hello",
            "description": "Hello",
            "short_description": "Hello",
            "time_to_read" : "8 min",
            "tags": "tecchnology,programming,coding",
        }
        form = PostForm(initial=data)
        context={
            "title" : "Create New Post",
            "form" : form,
        }
    return render(request, "posts/create.html", context=context)
