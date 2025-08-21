from rest_framework import generics
from .models import Curso
from .serializers import CursoSerializer


class CursoListCreateView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 


class CursoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer