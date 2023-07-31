from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm


@login_required(login_url="/users/login/")
def create_post(request):
    if request.method == 'POST':
        pass
    else:
        form = PostForm()
    context = {
        "title" : "Create New Post",
        "form" : form
    }
    return render(request, "posts/create.html", context=context)
