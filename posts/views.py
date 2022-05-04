from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    # if the method is POST
        # If the form is valid
        # yes    # Save
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else: 
            return HttpResponseRedirect(form.erros.as_json())
        # No, redirect error
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',
    {'posts':posts})

   

def delete(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    