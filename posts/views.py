from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from posts.models import Post, Autor, Conversa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import re

def index(request):
    postagem = Post.objects.all()
    response = {'postagens':postagem}
    return render(request, 'posts/index.html', response)

def about(request):
    return render(request, 'posts/about.html', {})

def enemies(request):
    authors = Autor.objects.all()
    resposta = {'autores': authors}
    return render(request, 'posts/enemies.html', resposta)

def chat(request):
    conversa = Conversa.objects.all()
    resposta = {'talks': conversa}
    if request.is_ajax():
        #titulo = request.PUT.get('titulo')
        #autor = request.user
        mensagem = request.GET.get('input_text')
        print(mensagem)
        print("oi")
        #Conversa.objects.create(post_author=autor,
                                #post_body=mensagem)
        #a = talker(mensagem)
        #Conversa.objects.create(post_author=autor,
                                #post_body=a)

        return JsonResponse({'data': "0"}, status=200)

    return render(request, 'posts/chat.html', resposta)

def submit_post(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        autor = request.POST.get('username')
        mensagem = request.POST.get('mensagem')
        Post.objects.create(post_title=titulo,
                            post_author=autor,
                            post_body=mensagem)

    return redirect('/posts')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/posts')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
        return redirect('/posts/pessoas/')

def char_login(request):
    if request.POST and 'login' in self.data:
        #username = Autor.objects.get(user_id=1)
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/posts')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
        return redirect('/posts/pessoas/')
    elif request.method == 'POST' and 'signup' in self.data:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm
    return render(request, 'posts/signup.html', {'form': form})

def signup(request):
    form = UserCreationForm()
    return render(request, 'posts/signup.html', {'form':form})

def talker(request):
    frase = request.split()
    if "oi" in frase:
        a = "tchau"
        return(a)
    #else:
    #    return redirect('/posts/chat/')

def submit_signup(request):
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        username = form.cleaned_data.get('username')
    #        raw_password = form.cleaned_data.get('password1')
    #        user = authenticate(username=username, password=raw_password)
    #        login(request, user)
    #        return redirect('/')
    #else:
    #    form = UserCreationForm
    #return render(request, 'posts/signup.html', {'form': form})
    if request.method == 'POST':
        #titulo = request.PUT.get('titulo')
        autor = request.user
        mensagem = request.POST.get('mensagem')
        Conversa.objects.create(post_author=autor,
                                post_body=mensagem)
        #a = talker(mensagem)
        #Conversa.objects.create(post_author=autor,
        #                       post_body=a)

    return redirect('/posts/chat/')

def noLoad(request):
    #if request.method == 'GET':
    if request.is_ajax:
        #titulo = request.PUT.get('titulo')
        #autor = request.user
        mensagem = request.GET.get('input_text')
        print(mensagem)
        #Conversa.objects.create(post_author=autor,
         #                       post_body=mensagem)
        a = talker(mensagem)
        #Conversa.objects.create(post_author=autor,
                               # post_body=a)

        return JsonResponse({'data': mensagem, 'b': a}, status=200)