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

#print(val)
print(val[5])
print("hola soy luis")
print("hola soy Carlos")
print("Hola, soy AstroErick")