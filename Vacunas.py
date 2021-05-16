# Necessary libraries
from typing import Tuple
from openpyxl import load_workbook
from openpyxl import Workbook
import time
import matplotlib.pyplot as plt

# This line stes the timer of a clock to measure computation time.
start = time.time()

# The datasheet is uploaded to the code so it can be read.
wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

# The fisrt line of the datasheet is read and the locations of the interest variables are deplyed.
tit = []
for row in sheet.iter_rows(min_row=1,max_row=1,values_only=True):
	tit += row
print(tit, "\n")

# After analysing the data, two lists of keywords were constructed. These incude word that may be found in text and also specific hashtags.
reactions = { "positive": ["safe", "treatment", "administration", "administered", "dose", "doses", "health", "healthy", "family", "admiration", "courage", "brave", "bravery", "serious", "seriously", "merry", "merrier","Same","paste", "effective", "healthcare", "stayhome", "stayathome", "covidiots", "stayathomesavelives", "crushcovid", "sciencematters", "dignity", "health", "hopenews", "scienceovermorons", "dignityhealth", "healthcareworker", "modernavaccine", "takethevaccine", "modern", "modernmedicine", "medicine", "vaccineday", "vaccinocovid", "frontlineworkers", "trustscience", "trust", "science", "facts", "fact", "sources", "source", "information", "cases", "case", "deaths", "distribution", "specialist", "programme", "inoculation", "inoculating", "needle", "medicine", "symptoms", "available", "update", "schedule", "immunity", "authorization", "authorized", "information", "approving", "approved", "manufacture", "manufacturing"],
"negative": ["bad", "crime", "cheat", "cheated", "greed", "side", "effects", "corruption", "hurt", "hurts", "hate", "hating", "diplomacy", "fake", "stall", "stalled", "war", "ineffective", "hesitation", "whereareallthesickpeople", "sick", "sick people"]}

# Some necessary vairbles are biuld.
vaccines = ["pfizer", "astrazeneca", "sputnikv", "moderna", "johnson", "oxford", "novavax", "sinovac", "cansino", "bharat"]
total_vaccines = {"pfizer": 0, "astrazeneca": 0, "sputnikv": 0, "moderna": 0, "johnson": 0, "oxford": 0, "novavax": 0, "sinovac": 0, "cansino": 0, "bharat": 0}

# Search of positive and negative tweets according to the keyword lists.
Pos = 0
Neg = 0
Neu = 0
total_words = dict()
for row in sheet.iter_rows(min_row = 2, max_row = sheet.max_row, values_only = True):
    rate = 0
    words = row[10].split()
    # This code line, does not really solves a problem, but it makes the clasification to work efficiently.
    if row[11] != None : hashtags = row[11].split("'")

    # Word are clasified and a global rate for the sentence is defined. The lower case convention is used in words and hashtags to avoid the consideration of repeated words with capital lettters present.
    for word in words:
        if word.lower() in reactions["positive"] : rate += 1
        elif word.lower() in reactions["negative"] : rate -= 1
    
        if word.lower() not in total_words : total_words[word.lower()] = 1
        elif word.lower() in total_words : total_words[word.lower()] += 1

        # Hashtags present in the text are tracked and appended to the corresponding hashtag list.
        if word[0] == "#" : hashtags.append(word[1:])
    
    # Now, the hashtags are analyazed.
    for hashtag in hashtags :

        # We've decided that this can affect the tweet's rate, as some intentions may not be totally considered.
        if hashtag.lower() in reactions["positive"] : rate += 1
        elif hashtag.lower() in reactions["negative"] : rate -= 1

        # The mention of some vaccines is counted and sotred in a dictionary.
        for vaccine in vaccines :
            if hashtag.lower()[0:len(vaccine)] == vaccine : total_vaccines[vaccine] += 1
    
    # the final rate defines whether the sentence is posotive, negative or neutral and these are counted.
    if rate >= 1 : Pos += 1
    elif rate <= -1 : Neg += 1
    else : Neu += 1

# Timer is terminated and results displayed.
end = time.time()
print("Positive: ", Pos, "\nNegative: ", Neg, "\nNeutral: ", Neu, "\nvaccines: ", total_vaccines, "\nTime: ", end - start)

# Fisrt try of an histogram (this is still in process).
plt.bar(total_vaccines.keys(), total_vaccines.values(), 1, color = 'b')
plt.show()