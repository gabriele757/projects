#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
# opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.aruodas.lt/butai/puslapis/2/"

driver.get(url)

time.sleep(10)

source = driver.page_source

bs = BeautifulSoup(source, 'html.parser')

ResultsSet = bs.find_all('div', {'class':'advert-flex'})
print(len(ResultsSet))

# Jūsų užduotis:
# Iš printinti linką, adresą, buto kainą, buto kainą už 1 kv metrą, vaizdas turi būti toks:
# ===SKELBIMAS===
# linkoas,
# adreas
# kaina
# kaina už 1 kv metrą

for skelbimas in ResultsSet:
    try:
        addres_element = skelbimas.find('div', {'class':'list-adress-v2'})
        tag = addres_element.find('h3').find('a', href=True)
        linkas = tag['href']
        # teksta galima pasiekti ir per
        # .contents atributa
        tekstas = tag.contents # jums grazina list objekta su teksto gabalais
        f   =  ''
        for i in tekstas:
            f = f + str(i).strip() # str - kad garantuotai butu tekstas
        adresas = f.replace('<br/>',', ')
        # tuo tarpu .text grazina centents teksta kaip vientisa
        # tekstas = tag.text.strip() # string metodas, skirtas pasalinti tarpus is pradzios ir pabaigos
        kainos = skelbimas.find('span', {'class':'list-item-price-v2'})
        txt = kainos.contents
        k  = ''
        for i in txt:
            k  = k  + str(i).strip()
        kaina = k.replace('</span>', ', ').replace(' ','').replace('€', '')
        kainos_kv = skelbimas.find('span',{'class':'price-pm-v2'})
        text = kainos_kv.contents
        kv =  ''
        for i in text:
            kv = kv + str(i).strip()
        kaina_kv = kv.replace('</span>', ', ').replace(' ','').replace('€/m²','')
        kambariai = skelbimas.find('div',{'class':'list-RoomNum-v2 list-detail-v2'})
        textk = kambariai.contents
        kam  = ''
        for i in textk:
            kam = kam + str(i).strip()
        kamb = kam.replace(' ','')
        print("====SKELBIMAS====")
        print(linkas)
        print(adresas)
        print(kaina)
        print(kaina_kv)
        print(kamb)
    except:
        pass

driver.close()

#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, kaina už 1 kv metrą, adresas, plotas, kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?