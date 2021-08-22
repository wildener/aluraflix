from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=50, null=False, unique=True)
    cor = models.CharField(max_length=7, null=False)  # cor da categoria no padrão RGB

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=100, null=False, unique=True)
    descricao = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=100, null=False, unique=True)
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_DEFAULT, default=1)  # default 1 = Categoria LIVRE

    def __str__(self):
        return self.titulo
