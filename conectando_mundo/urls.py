from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pais/', include('pais.urls')),
    path('api/',include('usuarios.urls')),
    path('curiosidades/', include('extra.urls')),
    path('', include('core.urls')),
]

    