#! D:\Pozyskiwanieigromadzeniedanych\myenv\Scripts\python.exe
import json
import os
import time
import bs4
import requests
from bs4 import BeautifulSoup

url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/dolnoslaskie/?page=1&search%5Bfilter_enum_builttype%5D%5B0%5D=blok&search%5Bfilter_enum_builttype%5D%5B1%5D=apartamentowiec&search%5Bfilter_enum_builttype%5D%5B2%5D=loft&search%5Bfilter_enum_builttype%5D%5B3%5D=pozostale&search%5Bfilter_enum_market%5D%5B0%5D=secondary/"

#adres url który zawiera następne strony z mieszkaniami
#https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/dolnoslaskie/?page=2&search%5Bfilter_enum_builttype%5D%5B0%5D=blok&search%5Bfilter_enum_builttype%5D%5B1%5D=apartamentowiec&search%5Bfilter_enum_builttype%5D%5B2%5D=loft&search%5Bfilter_enum_builttype%5D%5B3%5D=pozostale&search%5Bfilter_enum_market%5D%5B0%5D=secondary

r = requests.get(url)
if r.status_code == 200:
    print(f"strona dziala: {r}")
else: print(f"strona nie dziala!: {r}" )

# Parsowanie HTML za pomocą BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

#zapisywanie odpowiednich danych do tabeli
mieszkania = []
for flat_tag in soup.find_all('div', class_='css-1apmciz'):
    tytul = flat_tag.find('h6').text
    miejsce = flat_tag.find('p', class_='css-1a4brun er34gjf0').text
    cena = flat_tag.find('span', class_='css-643j0o').text
    ilosc_m = flat_tag.find('span', class_='css-643j0o').text
    flat_data = {
        'tytul': tytul,
        'cena': cena,
        'miejsce': miejsce,
        'metry': ilosc_m,
    }
    mieszkania.append(flat_data)
    
#zapisywanie pliku z danymi
with open('flats.json', 'w', encoding='utf-8') as file:
    json.dump(mieszkania, file)


#Stworzyć skrypt który dopisuje dane do pliku JOSN
#Stworzyć skrypt który czyta wiecej stron www od 1 do 25