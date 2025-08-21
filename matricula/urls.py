from django.urls import path
from . import views

urlpatterns = [
    
    path('matricula/', views.MatriculaListCreateView.as_view(), name='list-create-matricula'),
    path('matricula/<int:pk>', views.MatriculaRetrieveUpdateDestroy.as_view(), name='details-matricula'),

]
