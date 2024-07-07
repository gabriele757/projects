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

kaina_1 = []
kaina_kv_1 = []
adresas_1 = []
plotas_1 = []
kamb_1 = []
for puslapis in range(2,12):
    url = f"https://www.aruodas.lt/butai/puslapis/{puslapis}/"
    driver.get(url)
    time.sleep(15)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    ResultsSet = bs.find_all('div', {'class':'advert-flex'})
    for skelbimas in ResultsSet:
        try:
            addres_element = skelbimas.find('div', {'class':'list-adress-v2'})
            tag = addres_element.find('h3').find('a', href=True)
            linkas = tag['href']
            tekstas = tag.contents
            f   =  ''
            for i in tekstas:
               f = f + str(i).strip()
            adresas = f.replace('<br/>',', ')
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
            plt = skelbimas.find('div',{'class':'list-AreaOverall-v2 list-detail-v2'})
            txtpl = plt.contents
            plot = ''
            for i in txtpl:
                plot = plot + str(i).strip()
            plotas = plot.replace(' ','')
            adresas_1.append(adresas)
            kaina_1.append(float(kaina))
            kaina_kv_1.append(float(kaina_kv))
            plotas_1.append(float(plotas))
            kamb_1.append(float(kamb))
            print("====SKELBIMAS====")
            print(adresas)
            print(kaina)
            print(kaina_kv)
            print(kamb)
            print(plotas)
        except:
            pass

driver.close()

d = {'Adresas':adresas_1, 'Kaina':kaina_1, 'Kaina_uzkv':kaina_kv_1, 'Plotas':plotas_1, 'Kambariu_sk':kamb_1}
df = pd.DataFrame(data=d)
df.to_csv('aruodas04-22.csv', sep=';')


#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, 
# kaina už 1 kv metrą, adresas, plotas, kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. 
# Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, 
# daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?