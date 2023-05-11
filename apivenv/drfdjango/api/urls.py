from django.urls import path

from .views import Hello
from .views import CreateTarefas

urlpatters = [
    path('hello/', Hello.as_view(), name='hello'),
    # API Filmes
    path('Tarefas', CreateTarefas.as_view(), name='create-tarefas'),
]