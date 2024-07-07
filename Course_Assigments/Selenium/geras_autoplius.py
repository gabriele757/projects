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
for puslapis in range(2,5):
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
            gamintojas_1.append(gamintojomodelis)
    
            metai_kebulas = skelbimas.find('div',{'class':'announcement-title-parameters'})
            tag = metai_kebulas.find('div', {'class':'announcement-parameters'})
            amzius = tag.text.strip().split('\n')[0]
            kebulas = tag.text.strip().split('\n')[1]
            amzius_1.append(amzius)
            kebulas_1.append(kebulas)
            
            kainosvisos = skelbimas.find('div', {'class':'pricing-container has-loan-price'})
            tag = kainosvisos.find('div',{'class':'announcement-pricing-info'})
            kainos = tag.text.strip().split('\n')[0].replace(' ','').replace('€','')
            kaina_1.append(kainos)
        
            kuro_tipas = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = kuro_tipas.find('div', {'class':'announcement-parameters'})
            kuras = tag.text.strip().split('\n')[0]
            kuras_1.append(kuras)

            pavaru_dezes = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = pavaru_dezes.find('div', {'class':'announcement-parameters'})
            pavaru_deze = tag.text.strip().split('\n')[1]
            pavaros_1.append(pavaru_deze)
            
            turisinfo= skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = turisinfo.find('div', {'class':'announcement-parameters'})
            turis = tag.text.strip().split('\n')[3].replace(' ','').split(',')[0].replace('l','')
            turis_1.append(turis)

            galiainfo= skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = galiainfo.find('div', {'class':'announcement-parameters'})
            galia = tag.text.strip().split('\n')[3].replace(' ','').split(',')[1]#.replace('kW','')
            if 'kW' in galia:
                galia_1.append(galia)
            else:
                galia_1.append('Nenurodyta')
            
            ridosinfo = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = ridosinfo.find('div', {'class':'announcement-parameters'})
            ridos = tag.text.strip().split('\n')[4].replace(' ','').replace('km','')
            rida_1.append(ridos)
    
            miestuinfo = skelbimas.find('div',{'class':'announcement-parameters-block'})
            tag = miestuinfo.find('div', {'class':'announcement-parameters'})
            miestai = tag.text.strip().split('\n')[5]
            miestas_1.append(miestai)
            print ('====CIA KAZKOKIA INFO====')
            print(gamintojas_1, amzius_1,kebulas_1,kaina_1,kuras_1,pavaros_1,turis_1,galia_1,rida_1,miestas_1, sep ='\n')
        except Exception as klaida:
            print(klaida)

driver.close()

print(len(gamintojas_1))
print(len(amzius_1))
print(len(kebulas_1))
print(len(kaina_1))
print(len(kuras_1))
print(len(pavaros_1))
print(len(turis_1))
print(len(galia_1))
print(len(rida_1))
print(len(miestas_1))

# d = {'Gamintojas':gamintojas_1, 'Amzius':amzius_1, 'Kebulas':kebulas_1, 'Kaina':kaina_1, 'Kuras':kuras_1, 'Pavaros':pavaros_1, 'Turis':turis_1, 'Galia':galia_1, 'Rida':rida_1, 'Miestas':miestas_1}
# df = pd.DataFrame(data=d)
# df.to_csv('pabandymas.csv', sep=';')

