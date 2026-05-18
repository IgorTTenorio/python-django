from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index),
    path('imagem/', imagem, name='imagem'),
    path('imagem.html', imagem),
]
