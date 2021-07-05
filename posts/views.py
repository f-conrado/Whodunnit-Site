from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from posts.models import Post, Autor, Conversa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import re

def index(request):
    postagem = Post.objects.filter(post_author=2)
    response = {'postagens':postagem}
    return render(request, 'posts/index.html', response)

def about(request):
    person = request.user
    authors = Autor.objects.get(user=person)
    postagem = Post.objects.filter(post_author=authors.user_id)
    response = {'postagens': postagem, 'people': authors}
    return render(request, 'posts/about.html', response)

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

def amigos(request):
    return render(request, 'posts/amigos.html')

greetings = ["hi", "oi", "ola", "hello", "opa", "e ai"]
greetings_res = ["que foi?", "hey, you", "sup"]
default = ["you would say that"]

def talker(request):
    print(request)
    frase = ''.join(e for e in request if e.isalnum())
    print(frase)
    frase = frase.lower()
    frase = frase.split()
    for x in frase:
        if x in greetings:
            a = greetings_res[0]
            greetings_res.append(a)
            greetings_res.pop(0)
            print(greetings_res)
            return(a)
    return(default[0])

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
        #Conversa.objects.create(post_author=autor,
         #                       post_body=mensagem)
        a = talker(mensagem)
        #Conversa.objects.create(post_author=autor,
                               # post_body=a)

        return JsonResponse({'data': mensagem, 'b': a}, status=200)