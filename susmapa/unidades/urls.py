from django.urls import path
from .views import*

urlpatterns = [
    path('mapa/', mapa_unidades, name='mapa_unidades'),
    path('', home, name='home'),


]
