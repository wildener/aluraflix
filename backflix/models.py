from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100, null=False, unique=True)
    descricao = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.titulo
