from django.db import models
from django.utils import timezone


# Create your models here.
class Promocoes(models.Model):
    local = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_publicacao = models.TimeField(default=timezone.now)
    image_capa = models.ImageField(null=True, blank=True, upload_to='static/home/')


def __str__(self):
	return self.titulo
