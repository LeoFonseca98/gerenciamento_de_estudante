from django.contrib import admin
from .models import InscricaoDisciplina

@admin.register(InscricaoDisciplina)
class InscricaoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('disciplina_id', 'matricula_id',)
