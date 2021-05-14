from openpyxl import load_workbook
from openpyxl import Workbook

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]
