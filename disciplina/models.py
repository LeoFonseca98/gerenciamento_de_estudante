from django.db import models
from curso.models import Curso

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    curso_id = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __str__(self):
        return f"Disciplina: {self.nome}"
