from rest_framework import generics
from .models import Estudante
from .serializers import EstudanteSerializer

class EstudanteListCreateView(generics.ListCreateAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class EstudanteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
 
