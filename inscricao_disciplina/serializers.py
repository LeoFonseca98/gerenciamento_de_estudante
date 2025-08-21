from rest_framework import serializers
from .models import InscricaoDisciplina

class InscricaoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscricaoDisciplina
        fields = '__all__'