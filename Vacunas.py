from openpyxl import load_workbook
from openpyxl import Workbook

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

excel = load_workbook("vaccination_all_tweets.xlsx")
hoja = excel.worksheets[0]

for row in hoja.iter_rows(min_row=1,max_row=40,values_only=True):
    row



tit = []

for row in sheet.iter_rows(min_row=1,max_row=1,values_only=True):
	tit += row

print(tit)

val = []

for row in sheet.iter_rows(min_row=2,max_row=25,values_only=True):
    val += [row]

#print(val[5][2])
coor = []
for i in range(len(val)):
    coor.append([val[i][2]])
#print(coor)
a = val[5][10].split(" ")
#print(a)
#print("\n")
b = "Does"
for i in range(len(a)):
    if a[i] == b:
        print("Si es igual")

#for i in range(len(val[5][10]))
#print(val)
#print(val[5][10])
#print()

import requests
import urllib.parse

address = 'Birmingham, England'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = requests.get(url).json()
#print(response[0]["lat"])
#print(response[0]["lon"])

#diccionarios para filtrar

tf = ["Same", "said", "Same", "gato", "said", "said"]

reacciones = { "positivo": ["safe", "treatment", "administration", "administered", "dose", "doses", "health", "healthy", "family", "admiration", "courage", "brave", "bravery", "serious", "seriously", "merry", "merrier","Same","paste"],
"negativo": ["bad", "crime", "cheat", "cheated", "greed", "side", "effects", "corruption", "hurt", "hurts", "hate", "hating", "diplomacy", "fake", "stall", "stalled", "war"],
"neutral": ["facts", "fact", "sources", "source", "information", "cases", "case", "deaths", "distribution", "specialist", "programme", "inoculation", "inoculating", "needle", "medicine", "symptoms", "available", "update", "schedule", "immunity", "authorization", "authorized", "information", "approving", "approved", "manufacture", "manufacturing"]}

print("Parte del caliz")

dic = {
    "caliz": [["Same",0], ["said",0]]
}

for item in tf:
    for i in range(len(dic["caliz"])):
        if item == dic["caliz"][i][0]:
            dic["caliz"][i][1] += 1

print(dic)

print("Fin del caliz")

#vacunas = {"vacuna_general": ["pfizer", "astrazeneca", "sputnik", "moderna", "johnson", "oxford", "novavax", "sinovac", "cansino", "bharat"]}

P = 0
p = 0
N = 0
n = 0
for row in sheet.iter_rows(min_row=2,max_row=5,values_only=True):
    palabras = row[10].split()
    print(palabras)
    for item in palabras:
        if item in reacciones["positivo"]:
            p += 1
            print("Hola soy German")
        elif item in reacciones["negativo"]:
            n+=1
            print()
        else:
            print("no")
    P += p
    N += n
    p = 0
    n = 0

#búsqueda de tweets mediante palabras clave
"""
text = wb.worksheet[0]

for row in text[1:]:
    x = text.find(reacciones.values[0])
    text.find(row[10])
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