from django.db import models
from disciplina.models import Disciplina
from matricula.models import Matricula

class InscricaoDisciplina(models.Model):
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='disciplina')
    matricula_id = models.ForeignKey(Matricula, on_delete=models.PROTECT, related_name='matricula')

