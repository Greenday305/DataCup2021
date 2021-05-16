# Librerías necesarias para leer los datos.
from typing import Tuple
from openpyxl import load_workbook
from openpyxl import Workbook
import time

start = time.time()

# Se suben los datos y se selecciona la hoja a analizar.
wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

# Se leen los títulos para conocer la localización de los elementos a buscar y se despliegan.
# tit = []
# for row in sheet.iter_rows(min_row=1,max_row=1,values_only=True):
# 	tit += row
# print(tit)
########## INCLUIR ESTE CODIGO EN LA PRESENTACION ##############

reactions = { "positive": ["safe", "treatment", "administration", "administered", "dose", "doses", "health", "healthy", "family", "admiration", "courage", "brave", "bravery", "serious", "seriously", "merry", "merrier","Same","paste", "effective", "healthcare", "stayhome", "stayathome", "covidiots", "stayathomesavelives", "crushcovid", "sciencematters", "dignity", "health", "hopenews", "scienceovermorons", "dignityhealth", "healthcareworker", "modernavaccine", "takethevaccine", "modern", "modernmedicine", "medicine", "vaccineday", "vaccinocovid", "frontlineworkers", "trustscience", "trust", "science", "facts", "fact", "sources", "source", "information", "cases", "case", "deaths", "distribution", "specialist", "programme", "inoculation", "inoculating", "needle", "medicine", "symptoms", "available", "update", "schedule", "immunity", "authorization", "authorized", "information", "approving", "approved", "manufacture", "manufacturing"],
"negative": ["bad", "crime", "cheat", "cheated", "greed", "side", "effects", "corruption", "hurt", "hurts", "hate", "hating", "diplomacy", "fake", "stall", "stalled", "war", "ineffective", "hesitation", "whereareallthesickpeople", "sick", "sick people"]}

# vaccines_dict = {"PfizerBioNTech": 0, "AstraZeneca": 0, "SputnikV": 0, "Moderna": 0, "johnsonandjohnson": 0, "Oxford": 0, "Novavax": 0, "Sinovac": 0, "Cansino": 0, "Bharat": 0}
# vaccines = ["PfizerBioNTech", "AstraZeneca", "SputnikV", "Moderna", "johnsonandjohnson", "Oxford", "Novavax", "Sinovac", "Cansino", "Bharat"]

total_hashtags = dict()
vaccines = ["pfizer", "astrazeneca", "sputnikv", "moderna", "johnson", "oxford", "novavax", "sinovac", "cansino", "bharat"]
total_vaccines = {"pfizer": 0, "astrazeneca": 0, "sputnikv": 0, "moderna": 0, "johnson": 0, "oxford": 0, "novavax": 0, "sinovac": 0, "cansino": 0, "bharat": 0}
# Búsqueda de tweets mediante palabras clave
Pos = 0
Neg = 0
Neu = 0
total_words = dict()
for row in sheet.iter_rows(min_row = 2, max_row = sheet.max_row, values_only = True):
    rate = 0
    words = row[10].split()
    # Jajajaja este paso me da mucha risa, pero funciona "elegantemente".
    if row[11] != None : hashtags = row[11].split("'")
    for word in words:
        if word in reactions["positive"] : rate += 1
        elif word in reactions["negative"] : rate -= 1
    
        if word not in total_words : total_words[word] = 1
        elif word in total_words : total_words[word] += 1

        if word[0] == "#" : hashtags.append(word[1:])
    
    for hashtag in hashtags :
        if hashtag.lower() not in total_hashtags : total_hashtags[hashtag.lower()] = 1
        elif hashtag.lower() in total_hashtags : total_hashtags[hashtag.lower()] += 1

        if hashtag.lower() in reactions["positive"] : rate += 1
        elif hashtag.lower() in reactions["negative"] : rate -= 1

        for vaccine in vaccines :
            if hashtag.lower()[0:len(vaccine)] == vaccine : total_vaccines[vaccine] += 1
        
    if rate >= 1 : Pos += 1
    elif rate <= -1 : Neg += 1
    else : Neu += 1

end = time.time()
print("Positive: ", Pos, "\nNegative: ", Neg, "\nNeutral: ", Neu, "\nvaccines: ", total_vaccines, "\nTime: ", end - start)