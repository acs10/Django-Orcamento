from django.shortcuts import render
from .models import *

# Create your views here.
def orcamentos_lista(request):
    # logica
    orcamentos = Orcamento.objects.all()
    return render(request, 'mp_orcamento/orcamentos.html', {'orcamentos': orcamentos})


def orcamentos_estatisticas(request):
    maior_custo = 0
    menor_custo = 999999999999
    orcamento_maior_custo = None
    orcamento_menor_custo = None
    orcamentos = Orcamento.objects.all()
    somatorio_custo_total = 0
    for orcamento in orcamentos:
        somatorio = 0
        for peca in Peca.objects.filter(orcamento=orcamento):
            somatorio += peca.custo_de_producao_ajustado()
        orcamento.custo_total = somatorio * 1.25
        somatorio_custo_total += orcamento.custo_total
        if orcamento.custo_total >= maior_custo:
            orcamento_maior_custo = orcamento
            maior_custo = orcamento.custo_total
        if orcamento.custo_total <= menor_custo:
            orcamento_menor_custo = orcamento
            menor_custo = orcamento.custo_total
    quantidade = Orcamento.objects.count() 
    media_custo_total = somatorio_custo_total / quantidade
    return render(request, 'mp_orcamento/estatisticas.html', 
        {'quantidade': quantidade, 
        'orcamento_maior_custo': orcamento_maior_custo,
        'orcamento_menor_custo': orcamento_menor_custo,
        'media_custo_total': media_custo_total
        })
def info_cliente(request,id_cliente):
    clientes=Cliente.objects.get(pk=id_cliente)
    orcamento = Orcamento.objects.filter(cliente=clientes)
    return render(request, 'mp_orcamento/id_cliente.html',{'cliente': clientes, 'orcamento':orcamento})

def estatistica(request):
    maior_custo = 0
    menor_custo = 999999999999
    orcamento_maior_custo = None
    orcamento_menor_custo = None
    orcamentos = Cliente.objects.all()

    somatorio_custo_total = 0

    for orcamento in orcamentos:
        somatorio = 0

        for orcamento in Orcamento.objects.filter(cliente=orcamento):
            somatorio += orcamento.custo_total()

        orcamento.custo_total = somatorio
        
        if orcamento.custo_total >= maior_custo:
            orcamento_maior_custo = orcamento
            maior_custo = orcamento.custo_total

        if orcamento.custo_total <= menor_custo:
            orcamento_menor_custo = orcamento
            menor_custo = orcamento.custo_total

    quantidade = Cliente.objects.count()

    return render(request, 'mp_orcamento/estatistica.html', 
        {'quantidade': quantidade, 
        'orcamento_maior_custo': orcamento_maior_custo,
        'orcamento_menor_custo': orcamento_menor_custo,
        'maior_custo': maior_custo,
        'menor_custo': menor_custo}) 