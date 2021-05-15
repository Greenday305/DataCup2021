from openpyxl import load_workbook
from openpyxl import Workbook

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

tit = []

for row in sheet.iter_rows(min_row=1,max_row=1,values_only=True):
	tit += row

print(tit)

val = []

for row in sheet.iter_rows(min_row=2,max_row=25,values_only=True):
    val += [row]

print(val[5][2])
coor = []
for i in range(len(val)):
    coor.append([val[i][2]])
print(coor)
a = val[5][10].split(" ")
print(a)
print("\n")
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