from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('chat/submit', views.submit_signup),
    path('chat/send/', views.noLoad, name='send'),
    path('pessoas/', views.enemies, name='pessoas'),
    path('pessoas/submit', views.char_login),
    path('signup/', views.signup, name='signup'),
    path('signup/submit', views.submit_signup)
]