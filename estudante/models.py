from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    numero_matricula = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.nome} - {self.numero_matricula}"