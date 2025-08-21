from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('curso.urls')),
    path('api/v1/', include('disciplina.urls')),
    path('api/v1/', include('estudante.urls')),
    path('api/v1/', include('inscricao_disciplina.urls')),
    path('api/v1/', include('matricula.urls')),

]
