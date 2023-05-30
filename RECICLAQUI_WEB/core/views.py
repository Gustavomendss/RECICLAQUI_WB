from django.shortcuts import render
# Create your views here.

import requests
import json
from .models import todo
from django.shortcuts import render, HttpResponse
import pandas as pd
import folium
from folium import FeatureGroup
from folium.plugins import MarkerCluster
from folium.plugins import Geocoder
from geopy.distance import geodesic


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Welcome !</h1>")


def index(request):
    list_todo = todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})


def mark_as_done(request, id):
    obj = todo.objects.get(pk=id)
    obj.status = True
    obj.save()
    list_todo = todo.objects.filter(status=False)
    return render(request, 'base.html', {'list_todo': list_todo})


def new_todo(request):
    if request.method == "POST":
        todo.objects.create(name=request.POST.get('todo-name'))
        list_todo = todo.objects.filter(status=False)
        return render(request, 'base.html', {'list_todo': list_todo})


api_key = "639c8daf1b9941f28fd7c9e5d9bb2c07"
api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


def get_ip_geolocation_data(ip_address):
    # not using the incoming IP address for testing
    print(ip_address)
    response = requests.get(api_url)
    return response.content


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    geolocation_json = get_ip_geolocation_data(ip)
    geolocation_data = json.loads(geolocation_json)
    country = geolocation_data['country']
    region = geolocation_data['region']
    continent = geolocation_data['continent']

    return HttpResponse(
        "Welcome! Your IP address is: {} and you are visiting from {} in {}".format(ip, region, country, continent))


def geo_data(request):
    # ecopontos = pd.read_csv('RECICLAQUI_WEB/static/data/ecopontos.data')
    ecopontos_map = folium.Map(zoom_start=10, location=[-23.6616989, -46.7128187])

    # Get HTML Representation of Map Object
    ecopontos_map = ecopontos_map._repr_html_()
    context = {
        'map': ecopontos_map,
    }

    return render(request, "default.html", context)


def default_map(request):
    ecopontos_map = folium.Map(zoom_start=10, location=[-23.6616989, -46.7128187])
    return render(request, "default.html", {})


def maps(request):
   coordenadas = [-23.6616989, -46.7128187]

   map = folium.Map(coordenadas)
   folium.TileLayer('cartodbpositron').add_to(map)
   Geocoder().add_to(map)
   folium.Marker(coordenadas).add_to(map)
   folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
   folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
   folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
   folium.LayerControl().add_to(map)

   df = pd.read_csv("C:/Users/gusta/PycharmProjects/RECICLAQUI_PROJECT/data/ecopontos.csv")
   l = df.values.tolist()

   ecopontos = df
   # ecopontos = ecopontos[['latitude', 'longitude']]

   for i, r in ecopontos.iterrows():
       # setting for the popup
       popup = folium.Popup(r['NOME'], max_width=1000)
       # Plotting the Marker for each stationsト
       folium.map.Marker(
           location=[r['latitude'], r['longitude']],
           popup=popup,
           icon=folium.Icon(color="green", icon="fa-solid fa-recycle", prefix='fa')
       ).add_to(map)

   map = map._repr_html_()
   context = {
      'map': map,
             }
   return render(request, 'default.html', context)




def maps_teste(request):
   coordenadas = [-23.6616989, -46.7128187]

   map = folium.Map(location=coordenadas)
   folium.TileLayer('cartodbpositron').add_to(map)
   Geocoder().add_to(map)
   folium.Marker(coordenadas).add_to(map)
   folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
   folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
   folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
   folium.LayerControl().add_to(map)

   df = pd.read_csv("C:/Users/gusta/PycharmProjects/RECICLAQUI_PROJECT/data/ecopontos.csv")
   l = df.values.tolist()

   ecopontos = df
   # ecopontos = ecopontos[['latitude', 'longitude']]

   for i, r in ecopontos.iterrows():
       # setting for the popup
       popup = folium.Popup(r['NOME'], max_width=1000)
       # Plotting the Marker for each stationsト
       folium.map.Marker(
           location=[r['latitude'], r['longitude']],
           popup=popup,
           icon=folium.Icon(color="green", icon="fa-solid fa-recycle", prefix='fa')
       ).add_to(map)

   map = map._repr_html_()
   context = {
      'map': map,
             }
   return render(request, 'base.html', context)

