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