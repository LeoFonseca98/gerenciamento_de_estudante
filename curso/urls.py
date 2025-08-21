from django.urls import path
from . import views

urlpatterns = [

    path('curso/', views.CursoListCreateView.as_view(), name='list-create-curso'),
    path('curso/<int:pk>', views.CursoRetrieveUpdateDestroyView.as_view(), name='details-curso'),

    

]