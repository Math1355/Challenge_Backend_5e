from django.db import models
    
class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titulo
    
class Video(models.Model):
    titulo = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=300, default="")
    url = models.CharField(max_length=150, unique=True)
    """Ver uma forma de renomear o categoria para categoriaID"""
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.titulo
