from django.db import models
from datetime import datetime


# Create your models here.
class Promocoes(models.Model):
    local = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    publicacao_data_hora = models.DateTimeField(default=datetime.now)
    image_capa = models.ImageField(null=True, blank=True, upload_to='./static/home/')


def __str__(self):
    return self.titulo


CHOICES_ASSUNTOS = [
    ('', 'Selecione um assunto'),
    ('reserva', 'Reserva'),
    ('promoções', 'Promoções'),
    ('campeonatos de pesca', 'Campeonatos de Pesca'),
    ('dúvidas', 'Dúvidas'),
    ('elogios', 'Elogios'),
    ('reclamações', 'Reclamações')
]

# Create your models here.
class Contato(models.Model):
    assunto = models.CharField(choices=CHOICES_ASSUNTOS, default="", max_length=100)
    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)
