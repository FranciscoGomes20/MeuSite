from django.db import models


# Create your models here.
class Menssagens(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    menssagem = models.TextField()

    def __str__(self):
        return self.nome
