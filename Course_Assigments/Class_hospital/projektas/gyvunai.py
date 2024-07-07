import sqlite3

class Gyvunas:
    def __init__(self, vardas, amzius, svoris):
        self.vardas = vardas
        self.amzius = amzius
        self.svoris = svoris

class Prieglauda:
    def __init__(self):
        self.gyvunu_sarasas = []
    
    def prideti_gyvuna(self, gyvunas):
        self.gyvunu_sarasas.append(gyvunas)

    def istrinti_gyvuna(self, vardas):
        neistrinti  = []
        for gyvunas in self.gyvunu_sarasas:
            if vardas == gyvunas.vardas:
                neistrinti.append(gyvunas)
        self.gyvunu_sarasas = neistrinti

    # sukurti metodą, kuris grąžintų gyvūno objektą, kurio amžius yra lygus jūsų 
    # nurodytam amžiui

    def gyvunas_pagal_amziu(self, amzius):
        pagal_amziu  = []
        for gyvunas in self.gyvunu_sarasas:
            if amzius == gyvunas.amzius:
                pagal_amziu.append(gyvunas)
        return pagal_amziu


gyvunai = [{'vardas':'Brisius', 'amzius': 10}, {'vardas':'kate','amzius':5}]

prieglauda1 = Prieglauda()
prieglauda2 = Prieglauda()

gyvunas1 = Gyvunas('Testis', 4, 2)
gyvunas2 = Gyvunas('Brisius', 12, 25)
gyvunas3 = Gyvunas('Reksas', 7, 14)
# gyvunas3 = {'vardas':'kazkas','amzius':5, 'svoris':10}

prieglauda1.gyvunu_sarasas.append(gyvunas1)
prieglauda1.gyvunu_sarasas.append(gyvunas2)
prieglauda1.gyvunu_sarasas.append(gyvunas3)

print('----------------------')
for gyvunas in prieglauda1.gyvunu_sarasas:
    print(gyvunas.vardas)
print('----------------------')

# prieglauda1.prideti_gyvuna(gyvunas1)
# prieglauda1.prideti_gyvuna(gyvunas2)
prieglauda1.prideti_gyvuna(gyvunas3)

# print(prieglauda1.gyvunu_sarasas)
# print('----------------------')

prieglauda1.istrinti_gyvuna('Brisius')
print(prieglauda1.gyvunu_sarasas)
print('----------------------')

rezultatas = prieglauda1.gyvunas_pagal_amziu(4)
for gyvunas in rezultatas:
    print(gyvunas.vardas)

# prieglauda1.gyvunu_sarasas.append(gyvunas1)
# prieglauda1.gyvunu_sarasas.append(gyvunas2)
# prieglauda1.gyvunu_sarasas.append(gyvunas3)

print(prieglauda1.gyvunu_sarasas)
print('----------------------')
for gyvunas in prieglauda1.gyvunu_sarasas:
    print(gyvunas.vardas)
print('----------------------')

prieglauda1.prideti_gyvuna(gyvunas3)
for gyvunas in prieglauda1.gyvunu_sarasas:
    print(gyvunas.vardas)
print('----------------------')
# print(gyvunas3['vardas'])
# print(gyvunas1.vardas)

class Motociklas:
    def __init__ (self, marke, modelis, metai):
        self.marke = marke
        self.modelis = modelis
        self.metai = metai

    def uzkurti(self):
        print(f'Motociklas {self.marke} {self.modelis} buvo uzkurtas.')

motociklas1 = Motociklas('KTM', 'EXC450', 2016)
print(motociklas1.marke)
print(motociklas1.modelis)
print(motociklas1.metai)

motociklas1.uzkurti()

motociklas2 = Motociklas('Suzuki', 'DRZ400', 2006)
motociklas2.uzkurti()

motociklas = {'marke':'Honda','modelis':'CRF250','metai':2018}
print(motociklas['modelis'])

print(type(motociklas))
zodis = 'labas'
print(type(zodis))
zodis = zodis.upper()
print(zodis)

skaicius2 = 5
print(type(skaicius2))

print(type(motociklas1))


tv_kanalai = [{'pavadinimas':'LRT', 'programos': [{'savaites_diena':1, 'laidos':[{'laikas':'8:00', 'pavadinimas':'Gustavo Enciklopedija', 'dalyviai':[{'vardas':'Gustavas'}]}]}]}]
# pasiekti zodi Gustavas
# print(tv_kanalai[0]['programos'][0]['laidos'][0]['dalyviai'][0]['vardas'])

print(prieglauda1.gyvunu_sarasas[0].vardas)
print(type(prieglauda1.gyvunu_sarasas[0].vardas))


# sukurti klase fakultetas (pavadinimas, adresas, statybos metai)
# sukurti klase Universitetas, viena property - fakultetu_sarasas
# sukurti viena Universiteta
# suukurti kelis fakultetus

class Fakultetas:
    def __init__(self, pavadinimas, dekanas, statybos_metai, universiteto_id):
        self.pavadinimas = pavadinimas
        self.dekanas = dekanas
        self.statybos_metai = statybos_metai
        self.universiteto_id = universiteto_id

class Universitetas:
    def __init__(self):
        self.fakultetu_sarasas = []
        self.conn  = sqlite3.connect('universitetas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS universitetas
                            (universiteto_id INTEGER PRIMARY KEY,
                            pavadinimas TEXT)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS fakultetas
                            (fakulteto_id INTEGER PRIMARY KEY,
                            pavadinimas VARCHAR(50) NOT NULL,
                            dekanas TEXT,
                            statybos_metai TEXT,
                            universiteto_id INTEGER,
                            FOREIGN KEY(universiteto_id) REFERENCES universitetas(universiteto_id))
                            """)
        # self.cursor.execute("""INSERT INTO universitetas(pavadinimas) VALUES ('X Universitetas')""")
        self.conn.commit()

    def prideti_fakulteta(self, fakultetas):
        self.cursor.execute('INSERT INTO fakultetas (pavadinimas, dekanas, statybos_metai, universiteto_id) VALUES (?,?,?,?)', (fakultetas.pavadinimas, fakultetas.dekanas, fakultetas.statybos_metai, fakultetas.universiteto_id))
        # self.fakultetu_sarasas.append(fakultetas)
    
    def __del__ (self):
        self.conn.close()

    def spausdinti_universiteta(self):
        self.cursor.execute('SELECT * FROM universitetas')
        universitetai = self.cursor.fetchall()
        print('---------Universitetai---------')
        for universitetas in universitetai:
            print(universitetas)

    def spausdinti_fakulteta(self):
        self.cursor.execute('SELECT * FROM fakultetas')
        fakultetai = self.cursor.fetchall()
        print('---------Fakultetai------------')
        for fakultetas in fakultetai:
            print(fakultetas)

# sukurti du metodus 
# istrinti baznycia, kuri leis istrinti baznycia pagal baznycios pavadinima, pavadinima 
# turite pateikti kaip argumenta
# sukurti metoda, kuris leis atnaujinti informacija vienai baznyciai, naudokite input

    def istrinti_fakulteta(self, pavadinimas):
        self.cursor.execute('DELETE FROM fakultetas WHERE pavadinimas = ?', (pavadinimas,))
        rezultatas = self.cursor.fetchall()
        print('-------------------------------')
        print(f'{pavadinimas} fakultetas buvo istrintas.')

    def atnaujinti_fakulteta(self, pavadinimas):
        naujas_pavadinimas = input('Naujas fakulteto pavadinimas: ')
        naujas_dekanas = input('Naujas dekanas: ')
        nauji_statybos_metai = input('Nauji statybos metai: ')
        naujas_universiteto_id = input('Naujas universiteto id: ')
        self.cursor.execute('UPDATE fakultetas SET pavadinimas = ?, dekanas  = ?, statybos_metai =?, universiteto_id =? WHERE pavadinimas =?',(naujas_pavadinimas, naujas_dekanas, nauji_statybos_metai, naujas_universiteto_id, pavadinimas))
        print('-------------------------------')
        print(f'{pavadinimas} fakultetas atnaujintas sekmingai')


universitetas1 = Universitetas()
fakultetas1 = Fakultetas('Teises', 'Jonas Jonaitis', 1986,  1)
fakultetas2 = Fakultetas('Filosofijos','Petras Petrauskas', 1953, 1)
fakultetas3 = Fakultetas('Matematikos', 'Antanas Antanaitis', 1823, 1)
fakultetas4 = Fakultetas('Informatikos', 'Ona Onaitiene', 1824, 1)

universitetas1.prideti_fakulteta(fakultetas1)
universitetas1.prideti_fakulteta(fakultetas2)
universitetas1.prideti_fakulteta(fakultetas3)
universitetas1.prideti_fakulteta(fakultetas4)

# print('----------------------')
# for fakultetas in universitetas1.fakultetu_sarasas:
#     print(fakultetas.pavadinimas, fakultetas.dekanas, fakultetas.statybos_metai, fakultetas.universiteto_id)
print('-------------------------------')

universitetas1.spausdinti_universiteta()
universitetas1.spausdinti_fakulteta()
universitetas1.istrinti_fakulteta('Filosofijos')
universitetas1.spausdinti_fakulteta()
universitetas1.atnaujinti_fakulteta('Teises')
universitetas1.spausdinti_fakulteta()
