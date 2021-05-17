import folium
from folium.plugins import FastMarkerCluster
from openpyxl import load_workbook
import requests
import urllib.parse

locaciones = {}
with open("locaciones.txt") as f:
    for line in f:
        try:
            key, val = line.split(":")
            locaciones[key] = val
        except ValueError:
            pass

coor = []

for k in locaciones:
    b = locaciones[k].strip("'\n]['").split("', '")
    b = [ float(item) for item in b]
    locaciones[k] = [b,0]
    coor.append(b)

#list(locaciones.items())[0][1][2] = 5
#print(list(locaciones.values())[0][1])

#print(coor)
#print(len(coor))
#print(locaciones)

c = ['La Crescenta-Montrose, CA','Vancouver, BC - Canada','Vancouver, BC - Canada','Vancouver, BC - Canada','La Crescenta-Montrose, CA']

for item in c:
    if item in locaciones:
        locaciones[item][1] += 1

#print(locaciones)
print(locaciones.keys())
d = [list(locaciones.values())[i][1] for i in range(len(locaciones))]
print(d)

#Crear el mapa como un objeto
#m = folium.Map(location=[37.7790262, -122.419906])

#Otros marcadores #### ESTE ES EL DE FAST MARKER CLUSTER
#folium.plugins.FastMarkerCluster(coor,name='Tiendas de conveniencia').add_to(m)
#folium.map.LayerControl().add_to(m)

#Generar mapa, ya el html se abre en Chrome y muestra todo visual
#m.save('vis.html')

