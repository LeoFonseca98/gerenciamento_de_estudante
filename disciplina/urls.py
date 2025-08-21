from django.urls import path
from . import views

urlpatterns = [

    path('disciplina/', views.DisciplinaListCreateView.as_view(), name='list-create-disciplina'),
    path('disciplina/<int:pk>', views.DisciplinaRetrieveUpdateDestroyView.as_view(), name='details-disciplina'),

]
