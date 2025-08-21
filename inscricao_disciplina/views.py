from rest_framework import generics
from .models import InscricaoDisciplina
from .serializers import InscricaoDisciplinaSerializer

class InscricaoDisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = InscricaoDisciplina.objects.all()
    serializer_class = InscricaoDisciplinaSerializer

class InscricaoDisciplinaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InscricaoDisciplina.objects.all()
    serializer_class = InscricaoDisciplinaSerializer
