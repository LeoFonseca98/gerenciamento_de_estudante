from django.urls import path
from . import views

urlpatterns = [
    
    path('estudante/', views.EstudanteListCreateView.as_view(), name='list-create-estudante'),
    path('estudante/<int:pk>', views.EstudanteRetrieveUpdateDestroy.as_view(), name='details-estudante'),

]
