import folium
from folium.plugins import FastMarkerCluster
from openpyxl import load_workbook
import requests
import urllib.parse

f = open("coor.txt","a")

wb = load_workbook('vaccination_all_tweets.xlsx')
sheet = wb.worksheets[0]

for row in sheet.iter_rows(min_row=31435, max_row=31437, values_only=True):
    try:
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(row[2]) +'?format=json'
        response = requests.get(url).json()
        cor = [row[2], [ response[0]["lat"] , response[0]["lon"]]]
        f.write(f'{cor}\n')
    except TypeError:
        pass
    except IndexError:
        pass
    except ConnectionResetError:
        f.close()
    except ConnectionAbortedError:
        f.close()
    except ConnectionRefusedError:
        f.close()
    except ConnectionError:
        f.close()

f.close()