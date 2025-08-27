from django.urls import path
from . import views

urlpatterns = [
    path('personalidades_historicas/', views.personalidades_historicas, name='personalidades_historicas'),
]