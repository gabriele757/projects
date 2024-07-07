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

gamintojas_1 = []
amzius_1 = []
kebulas_1 = []
kaina_1 = []
kuras_1 = []
pavaros_1 = []
turis_1 = []
galia_1 = []
rida_1 = []
miestas_1 = []
for puslapis in range(2,3):
    url = f"https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={puslapis}"
    driver.get(url)
    time.sleep(15)
    source = driver.page_source
    bs = BeautifulSoup(source, 'html.parser')
    ResultsSet = bs.find_all('div', {'class':'announcement-content'})
    print(len(ResultsSet))
    for skelbimas in ResultsSet:
        try:
            print('====SKELBIMAS====')
            gamintojas = skelbimas.find('div',{'class':'announcement-body-heading'})
            tag = gamintojas.find('div', {'class':'announcement-title'})
            gamintojomodelis = tag.text.strip()
            d = {'Gamintojas ir modelis':gamintojomodelis}
            gamintojas_1.append(d)
            print(d)
            metai_kebulas = skelbimas.find('div',{'class':'announcement-title-parameters'})
            tag = metai_kebulas.find('div', {'class':'announcement-parameters'})
            amzius = float(tag.text.strip()[:4])
            kebulas = tag.text.strip().split('\n')[1]
            m = {'Amzius': amzius}
            amzius_1.append(m)
            print(m)
            keb = {'Kebulo tipas': kebulas}
            kebulas_1.append(keb)
            print(keb)
            kainosvisos = skelbimas.find('div', {'class':'pricing-container has-loan-price'})
            tag = kainosvisos.find('div',{'class':'announcement-pricing-info'})
            kainos = float(tag.text.strip().split('\n')[0].replace(' ','').replace('€',''))
            kn = {'Kaina': kainos}
            kaina_1.append(kn)
            print(kn)
            kuro_tipas = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = kuro_tipas.find('div', {'class':'announcement-parameters'})
            kuras = tag.text.strip().split('\n')[0]
            kr = {'Kuras':kuras}
            kuras_1.append(kr)
            print(kr)
            pavaru_dezes = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = pavaru_dezes.find('div', {'class':'announcement-parameters'})
            pavaru_deze = tag.text.strip().split('\n')[1]
            pav_deze = {'Pavaru deze':pavaru_deze}
            pavaros_1.append(pav_deze)
            print(pav_deze)
            turisinfo= skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = turisinfo.find('div', {'class':'announcement-parameters'})
            turis = tag.text.strip().split('\n')[3].replace(' ','').split(',')[0].replace('l','')
            tur = {'Turis':turis}
            turis_1.append(tur)
            print(tur)
            galiainfo= skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = galiainfo.find('div', {'class':'announcement-parameters'})
            galia = tag.text.strip().split('\n')[3].replace(' ','').split(',')[1].replace('kW','')
            gal = {'Galia':galia}
            galia_1.append(gal)
            print(gal)
            ridosinfo = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = ridosinfo.find('div', {'class':'announcement-parameters'})
            ridos = tag.text.strip().split('\n')[4].replace(' ','').replace('km','')
            rida = {'Rida':ridos}
            rida_1.append(rida)
            print(rida)
            miestuinfo = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = miestuinfo.find('div', {'class':'announcement-parameters'})
            miestai = tag.text.strip().split('\n')[5]
            miestas =  {'Miestas': miestai}
            miestas_1.append(miestas)
            print(miestas)
            print ('====CIA KAZKOKIA INFO====')
            print(gamintojas_1)
        except:
            pass

driver.close()

# d = {'Gamintojas':gamintojas_1, 'Amzius':amzius_1, 'Kebulas':kebulas_1, 'Kaina':kaina_1, 'Kuras':kuras_1, 'Pavaros':pavaros_1, 'Turis':turis_1, 'Galia':galia_1, 'Rida':rida_1, 'Miestas':miestas_1}
# df = pd.DataFrame(data=d)
# df.to_csv('aruodas04-22.csv', sep=';')

