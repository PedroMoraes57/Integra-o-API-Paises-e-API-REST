from django.urls import path
from . import views
from .views import UsuarioViewSet
from rest_framework .routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('cadastro_usuarios/', views.cadastro_usuarios, name='cadastro_usuarios'),
    path('parceiros/', views.UsuariosAPI, name='parceiros'),
    path('executar_testes/', views.executar_testes_usuarios, name='teste_usuarios') 
]

urlpatterns += router.urls