from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.titulo
