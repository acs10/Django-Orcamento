from django.urls import path
from .views import *

urlpatterns = [
    path('orcamentos/', orcamentos_lista, name='orcamentos-lista'),
    path('orcamentos/estatisticas/', orcamentos_estatisticas, name='orcamentos-estatisticas'),
    path('orcamentos/cliente/<int:id_cliente>/', info_cliente, name='info_cliente'),
    path('orcamentos/cliente/estatistica/', estatistica, name='estatistica'),
    
]
