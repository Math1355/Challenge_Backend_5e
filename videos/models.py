from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=300)
    url = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.titulo
