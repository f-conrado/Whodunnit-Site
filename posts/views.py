from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def index(request):
    postagem = Post.objects.all()
    response = {'postagens':postagem}
    return render(request, 'posts/index.html', response)

def about(request):
    return render(request, 'posts/about.html', {})

def enemies(request):
    return render(Post)
