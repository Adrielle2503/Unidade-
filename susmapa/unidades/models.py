from django.db import models

class UnidadeSaude(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)  # UPA, UBS, etc.
    endereco = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    medicamentos_disponiveis = models.TextField(blank=True)  # Lista simples por enquanto
    especialidades = models.TextField(blank=True)

    def __str__(self):
        return self.nome

