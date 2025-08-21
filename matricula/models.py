from django.db import models
from estudante.models import Estudante
from curso.models import Curso


class Matricula(models.Model):
    estudante_id = models.ForeignKey(Estudante,  on_delete=models.PROTECT, related_name='estudante')
    curso_id = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='curso')
    data_matricula = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Estudante:{self.estudante_id} - Curso:{self.curso_id} - Data:{self.data_matricula}"