from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

    def __str__(self):
        return self.nome


class Orcamento(models.Model):
    data_hora = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.data_hora, self.cliente.nome)

    def custo_total(self):
        somatorio = 0
        for peca in Peca.objects.filter(orcamento=self):
            somatorio += peca.custo_de_producao_ajustado()
        return somatorio * 1.25


class Peca(models.Model):
    tipo_da_mobilia = models.CharField(max_length=64)
    largura = models.FloatField()
    altura = models.FloatField()
    profundidade = models.FloatField()
    tipo_do_puxador = models.CharField(max_length=64)
    pintura = models.CharField(max_length=64)
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_da_mobilia

    def area_total(self):
        area_frente = self.largura * self.altura
        area_lado = self.altura * self.profundidade
        area_total = area_frente + area_frente + area_lado + area_lado
        # converte de cm para m
        area_total = area_total / 100        
        return area_total

    def custo_de_producao(self):
        area_total = self.area_total()
        custo_de_producao = 0
        if self.tipo_da_mobilia == 'compartimento de armário':
            custo_de_producao += 50 * area_total
        else:
            custo_de_producao += 75 * area_total
        if self.tipo_do_puxador == 'plástico':
            custo_de_producao += 5
        else:
            custo_de_producao += 8.5
        if self.pintura == 'acabamento PU':
            custo_de_producao += 15 * area_total
        elif self.pintura == 'acabamento PU texturizado':
            custo_de_producao += 20 * area_total
        else:
            custo_de_producao += 35 * area_total
        return custo_de_producao

    def custo_de_producao_ajustado(self):
        return self.custo_de_producao() * 1.75 