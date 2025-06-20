from django.shortcuts import render
import folium
from .models import UnidadeSaude



def home(request):
    return render(request, 'unidades/home.html')
def mapa_unidades(request):
    unidades = UnidadeSaude.objects.all()

    mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

    for unidade in unidades:
        folium.Marker(
            [unidade.latitude, unidade.longitude],
            popup=f"<b>{unidade.nome}</b><br>{unidade.tipo}<br>{unidade.medicamentos_disponiveis}"
        ).add_to(mapa)

    mapa = mapa._repr_html_()

    return render(request, 'unidades/mapa.html', {'mapa': mapa})
