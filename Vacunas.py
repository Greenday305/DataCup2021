# Librerías necesarias para leer los datos.
from typing import Tuple
from openpyxl import load_workbook
from openpyxl import Workbook

# Se suben los datos y se selecciona la hoja a analizar.
wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

# Se leen los títulos para conocer la localización de los elementos a buscar y se despliegan.
tit = []
for row in sheet.iter_rows(min_row=1,max_row=1,values_only=True):
	tit += row
print(tit)
print("\n")

# Con lo anterior en mente, se leen los tweets
tweet_range = (2,sheet.max_row)
tweets = []
index = 0
for row in sheet.iter_rows(min_row=tweet_range[0], max_row=tweet_range[1], values_only=True):
    tweets += [row]
    print(tweets[index][10])
    print("\n")
    index += 1
# coor = []
# for i in range(len(val)):
#     coor.append([val[i][2]])
# print(coor)
# a = val[5][10].split(" ")
# print(a)
# print("\n")
# b = "Does"
# for i in range(len(a)):
#     if a[i] == b:
#         print("Si es igual")

#for i in range(len(val[5][10]))
#print(val)
#print(val[5][10])
#print()

import requests
import urllib.parse

address = 'Birmingham, England'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
print("\n")
print(response[0]["lat"])
print(response[0]["lon"])

#diccionarios para filtrar

reacciones = { "positivo": ["safe", "treatment", "administration", "administered", "dose", "doses", "health", "healthy", "family", "admiration", "courage", "brave", "bravery", "serious", "seriously", "merry", "merrier"],
"negativo": ["bad", "crime", "cheat", "cheated", "greed", "side", "effects", "corruption", "hurt", "hurts", "hate", "hating", "diplomacy", "fake", "stall", "stalled", "war"],
"neutral": ["facts", "fact", "sources", "source", "information", "cases", "case", "deaths", "distribution", "specialist", "programme", "inoculation", "inoculating", "needle", "medicine", "symptoms", "available", "update", "schedule", "immunity", "authorization", "authorized", "information", "approving", "approved", "manufacture", "manufacturing"]}

vacunas = {"vacuna_general": ["pfizer", "astrazeneca", "sputnik", "moderna", "johnson", "oxford", "novavax", "sinovac", "cansino", "bharat"],
"pfizer": "pfizer",
"aztrazeneca": "astrazeneca",
"sputnik": "sputnik",
"moderna": "moderna", 
"johnson": "johnson", 
"oxford": "oxford",
"novavax": "novavax",
"sinovac": "sinovac",
"cansino": "cansino",
"bharat": "bharat"}

#búsqueda de tweets mediante palabras clave
"""
text = wb.worksheet[10]

for row in text[1:]:
    x = text.find(reacciones.values[0])
    if x == True:
        print(x)

for row in text[1:]:
    y = text.find(reacciones.values[1])
    if y == True:
        print(y)

for row in text[1:]:
    z = text.find(reacciones.values[2])
    if z == True:
        print(z)

for row in text[1:]:
    v1 = text.find(vacunas.values[0])
    if v1 == True:
        print(v1)

for row in text[1:]:
    v2 = text.find(vacunas.values[1])
    if v2 == True:
        print(v2)

for row in text[1:]:
    v3 = text.find(vacunas.values[2])
    if v3 == True:
        print(v3)

for row in text[1:]:
    v4 = text.find(vacunas.values[3])
    if v4 == True:
        print(v4)

for row in text[1:]:
    v5 = text.find(vacunas.values[4])
    if v5 == True:
        print(v5)

for row in text[1:]:
    v6 = text.find(vacunas.values[5])
    if v6 == True:
        print(v6)

for row in text[1:]:
    v7 = text.find(vacunas.values[6])
    if v7 == True:
        print(v7)

for row in text[1:]:
    v8 = text.find(vacunas.values[7])
    if v8 == True:
        print(v8)

for row in text[1:]:
    v9 = text.find(vacunas.values[8])
    if v9 == True:
        print(v9)

for row in text[1:]:
    v10 = text.find(vacunas.values[9])
    if v10 == True:
        print(v10)

for row in text[1:]:
    v11 = text.find(vacunas.values[10])
    if v11 == True:
        print(v11)
"""