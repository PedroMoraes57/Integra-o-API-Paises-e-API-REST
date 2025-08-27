from django.urls import path
from . import views

urlpatterns = [
    path('franca/', views.busca_pais, name='busca_pais'),
]