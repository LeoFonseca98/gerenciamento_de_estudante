from django.db import models

class Curso(models.Model):
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]

    nome = models.CharField(max_length=255)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)


    def __str__(self):
        return f"{self.nome} - {self.turno}"
