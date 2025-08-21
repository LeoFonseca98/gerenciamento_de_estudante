from django.urls import path
from . import views

urlpatterns = [

    path('inscricao/', views.InscricaoDisciplinaListCreateView.as_view(), name='list-create-inscricao'),
    path('inscricao/<int:pk>', views.InscricaoDisciplinaRetrieveUpdateDestroy.as_view(), name='details-inscricao'),
]


