import folium
from folium.plugins import FastMarkerCluster
from openpyxl import load_workbook

#Crear el mapa como un objeto
m = folium.Map(location=[19.595772, -98.997218])

#Global tooltip
#tooltip = "Click para más información"

#Procesamiento del excel de Kelloggs

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

coordenadas = []

for row in sheet.iter_rows(min_row=2,values_only=True):
	xy = [ row[0] , row[1]]
	if xy not in coordenadas:
		coordenadas.append(xy)

#Marcadores para cada objeto
#for item in coordenadas:
#	folium.map.Marker(item,
#				popup='<strong>Tiendita</strong>',
#				tooltip=tooltip).add_to(m)


#Otros marcadores
folium.plugins.FastMarkerCluster(coordenadas,name='Tiendas de conveniencia').add_to(m)
folium.map.LayerControl().add_to(m)

#Añadir una línea de varios puntos
#folium.vector_layers.PolyLine(coordenadas).add_to(m)

#Generar mapa, ya el html se abre en Chrome y muestra todo visual
#m.save('map.html')
m.save('tweets.html')