import selenium
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time # dėl sleep komandos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

opcijos = Options()
# opcijos.add_argument('--incognito')  #kad atidarytu narsykle incognito rezimu

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"  #kuri norime atsidaryti

driver.get(url) #atidaromas puslapis
time.sleep(3) #nurodoma kiek laiko pasnausti

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') #teoriskai isparsinimo puslapio html
ResultsSet = bs.find_all('a', {'class':'articles-list-title'})
pavadinimai = []
for elementas in ResultsSet:
    print("::ELEMENTAS::")
    print(elementas)
    print(elementas['href'])  # ['href'] is atrinktos klases leidzia gauti link'a (nuoroda, adresa)
    pavadinimai.append(elementas.text) # pasiekiame elemente esanti teksta, siuo atveju - straipsnio pavadinima
print(pavadinimai)


simboliai = []
for simb in pavadinimai:
    simboliai.append(len(simb))
print(simboliai)
zodziai = []
for item in pavadinimai:
    zodziai.append(len(item.split()))
print(zodziai)

df = pd.DataFrame()
df['pavadinimai'] = pavadinimai
df['zodziu_kiekis'] = zodziai
df['simboliu_kiekis'] = simboliai
df.to_csv('uzduotis.csv', sep=';')

#Surinkite visus kauno dienos straipsnių pavadinimus į pandas dataframe.
#pridėkite naują stulpelį, kuriame būtų žodžių kiekis kiekviename pavadinime
#pridėkite naują stulpelį, kuriame būtų pavadinime esančių simbolių kiekis
#eksportuokite tai į CSV failą
# driver.close()