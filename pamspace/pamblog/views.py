from django.shortcuts import render
from pamblog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
    })

def content(request, id):
    content = Post.objects.get(id=id)
    return render(request, 'content.html', {
        'content': content,
    })
