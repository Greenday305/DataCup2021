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