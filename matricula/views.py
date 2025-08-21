from rest_framework import generics
from .models import Matricula
from .serializers import MatriculaSerializer


class MatriculaListCreateView(generics.ListCreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

