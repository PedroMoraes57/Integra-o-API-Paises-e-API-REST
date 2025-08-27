
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.contrib import messages
from .serializers import UsuarioSerializer
from rest_framework import viewsets
import requests
import subprocess
import sys

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def cadastro_usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render (request,'usuarios/cadastro_usuarios.html',{'form':form})
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
def UsuariosAPI(request):
    lista_usuarios_url = f'http://10.90.238.2:8000/usuario/' 
    lista = []
    try:
        response = requests.get(lista_usuarios_url, timeout=5)
        response.raise_for_status()
        lista = response.json()
    except requests.exceptions.RequestException as e:
        messages.error(request, f'Erro ao consultar API: {e}')
    context = {
        'lista': lista,
    }
    return render(request, 'usuarios/parceiros.html', context)

def executar_testes_usuarios(request):
    string_testes = ""
    if request.method == "POST":
        try:
            resultado_testes = subprocess.run(
                [sys.executable, 'manage.py', 'rodar_testes_usuarios'],
                capture_output= True,
                text= True,
                encoding= 'utf-8',
                errors= 'replace',
                check= True
            )
            string_testes = resultado_testes.stdout
        except subprocess.CalledProcessError as e:
            string_testes = f"Erro: {e.stderr}"
        except Exception as e:
            string_testes = f"Erro não esperado {str(e)}"
    return render(request, 'usuarios/pagina_testes.html', {"string_testes":string_testes})