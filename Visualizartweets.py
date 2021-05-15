import folium
from folium.plugins import FastMarkerCluster
from openpyxl import load_workbook
import requests
import urllib.parse

#Crear el mapa como un objeto
m = folium.Map(location=[37.7790262, -122.419906])

#Global tooltip
#tooltip = "Click para más información"

#Procesamiento del excel de Kelloggs

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

coordenadas = []

i=2
for row in sheet.iter_rows(min_row=2,max_row=46060,values_only=True):
    address = row[2]
    while True:
        try:
            url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
            response = requests.get(url).json()
            xy = [ response[0]["lat"] , response[0]["lon"]]
            print([row[2],xy])
            coordenadas.append(xy)
            #i+=1
            break
        except TypeError:
            #i+=1
            print([row[2],"Este no"])
            break
        except IndexError:
            print([row[2],"IndexError (checar)"])
            break
        


#Marcadores para cada objeto
#for item in coordenadas:
#	folium.map.Marker(item,
#				popup='<strong>Tiendita</strong>',
#				tooltip=tooltip).add_to(m)


#Otros marcadores #### ESTE ES EL DE FAST MARKER CLUSTER
folium.plugins.FastMarkerCluster(coordenadas,name='Tiendas de conveniencia').add_to(m)
folium.map.LayerControl().add_to(m)

#Añadir una línea de varios puntos
#folium.vector_layers.PolyLine(coordenadas).add_to(m)

#Generar mapa, ya el html se abre en Chrome y muestra todo visual
#m.save('map.html')
m.save('tweets.html')