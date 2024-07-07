import sqlite3
import datetime 
# Jūsų užsakovas yra smulkus autoservisas, kuriam yra reikalinga registracijos sistema
# Autoservisas nori kaupti informaciją apie:

    # 1. Mechanikus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas
        # 4. valandinis_atlyginimas
        # 5. specializacija (elektra/važiuoklė/variklis/kėbulai)

    # 2. Klientus:
        # 1. vardas
        # 2. pavardė
        # 3. el_paštas

    # 3. Klientų automobilius:
        # 1. Valstybinis numeris
        # 2. Markė
        # 3. Modelis
        # 4. Savininkas

    # 4. Remontus:
        # 1. kliento_id
        # 2. mechaniko_id
        # 3. darbo_pradzia
        # 4. darbo_pabaiga
        # 5. darbo kaina (darbo_pabaiga - darbo_pradzia) x mechaniko valandinis įkainis x 2 (autoserviso dalis)
        # 6. remonto_kategorija (elektra/važiuoklė/variklis/kėbulai)

# jums taip pat reikės lentelės autoservisas, kuriame bus laikoma visa informacija.

# turint šias žinias jums reikės sukurti sistemą, valdomą per terminalą, vartotojas įjungęs aplikaciją, gali pasirinkti šiuos žingsnius:

# 1. pridėti:
    # 1. mechaniką
    # 2. klientą
    # 3. kliento automobilį
    # 4. remontą

# 2. parodyti visus:
    # 1. mechanikus
    # 2. klientus
    # 3. klientų automobilus
    # 4. remontus

# papildomos užduotys, jas iškviesti reikia terminale nurodant veiksmo numerį/įvedant skaičių:

# patobulinkite funkciją, kuri prieš pridedant remontą patikrintų ar tuo metu, kai klientas pageidauja remontuoti automobilį yra laisvų automechanikų
# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už visų savo automobilių visus remontus
# sukurkite funkciją, kuri apskaičiuotų, kiek vienas klientas yra mums sumokėjęs iš viso už vieno konkretaus automobilio remontą
# sukurkite funkciją, kuri apskaičiuotų kiek uždirbo konkretus mechanikas X

class Mechanikas:
    def __init__(self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.valandinis_atlyginimas = valandinis_atlyginimas
        self.specializacija = specializacija

class Klientas:
    def __init__(self, vardas, pavarde, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas

class Automobilis:
    def __init__(self, valstybinis_numeris, marke, modelis, kliento_id):
        self.valstybinis_numeris = valstybinis_numeris
        self.marke = marke
        self.modelis = modelis
        self.kliento_id = kliento_id

class Remontas:
    def __init__(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija):
        self.kliento_id = kliento_id
        self.mechaniko_id = mechaniko_id
        self.darbo_pradzia = darbo_pradzia
        self.darbo_pabaiga = darbo_pabaiga
        self.darbo_kaina = darbo_kaina
        self.remonto_kategorija = remonto_kategorija

class Autoservisas:
    def __init__(self):
        self.conn = sqlite3.connect('autoservisas.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(""" CREATE TABLE IF NOT EXISTS mechanikai(
               mechaniko_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               el_pastas TEXT,
               valandinis_atlyginimas REAL,
               specializacija VARCHAR(50) NOT NULL)""")
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS klientai(
               kliento_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               el_pastas TEXT)""")
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS automobiliai(
               automobilio_id INTEGER PRIMARY KEY,
               valstybinis_numeris TEXT,
               marke TEXT,
               modelis TEXT,
               kliento_id INTEGER,
               FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id))""")
        self.cursor.execute("""
               CREATE TABLE IF NOT EXISTS remontai(
               remonto_id INTEGER PRIMARY KEY,
               kliento_id INTEGER,
               mechaniko_id INTEGER,
               darbo_pradzia DATE,
               darbo_pabaiga DATE,
               darbo_kaina REAL,
               remonto_kategorija TEXT,
               FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id),
               FOREIGN KEY (mechaniko_id) REFERENCES mechanikas(mechaniko_id))""")
        self.conn.commit()
        
    def prideti_mechanika(self, vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija):
        mechanikas = Mechanikas(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija)
        self.cursor.execute("INSERT INTO mechanikai (vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija) VALUES (?, ?, ?, ?, ?)", (vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija))
        self.conn.commit()
        return mechanikas
    
    def prideti_klienta(self, vardas, pavarde, el_pastas):
        klientas = Klientas(vardas, pavarde, el_pastas)
        self.cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)", (vardas, pavarde, el_pastas))
        self.conn.commit()
        return klientas
    
    def prideti_automobili(self, valstybinis_numeris, marke, modelis, kliento_id):
        automobilis = Automobilis(valstybinis_numeris, marke, modelis, kliento_id)
        self.cursor.execute("INSERT INTO automobiliai (valstybinis_numeris, marke, modelis, kliento_id) VALUES (?, ?, ?, ?)", (valstybinis_numeris, marke, modelis, kliento_id))
        self.conn.commit()
        return automobilis
    
    def prideti_remonta(self, kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija):
        remontas = Remontas(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina = 1, remonto_kategorija=remonto_kategorija)
        date_format = "%Y-%m-%d %H:%M"
        darbo_pradzia_date = datetime.datetime.strptime(darbo_pradzia, date_format)
        darbo_pabaiga_date = datetime.datetime.strptime(darbo_pabaiga, date_format)
        valandos = darbo_pabaiga_date - darbo_pradzia_date
        valandos = valandos.total_seconds()/3600
        valandinis_atlyginimas = self.gauti_valandini_ikaini(mechaniko_id)
        darbo_kaina = valandos * valandinis_atlyginimas *2
        self.cursor.execute("INSERT INTO remontai (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija) VALUES (?, ?, ?, ?, ?, ?)", (kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, darbo_kaina, remonto_kategorija))
        self.conn.commit()
        return remontas
    
    def gauti_valandini_ikaini(self, mechaniko_id):
       self.cursor.execute(f'SELECT valandinis_atlyginimas from mechanikai WHERE mechaniko_id = {mechaniko_id}')
       valandinis = self.cursor.fetchone()
       print(valandinis)
       return float(valandinis[0])

    def perziureti_irasus(self, lentele):
        self.cursor.execute(f'SELECT * FROM {lentele}')
        rezultatu_sarasas = self.cursor.fetchall()
        print('\nĮrašai pagal jūsų užklausą: ')
        for rezultatas in rezultatu_sarasas:
            print(rezultatas)

    def apskaiciuoti_visus_remontus_pagal_kliento_id(self, kliento_id):
        self.cursor.execute(f'Select SUM(darbo_kaina) FROM remontai WHERE kliento_id = {kliento_id}')
        rezultatai = self.cursor.fetchall()
        print(rezultatai)
        return rezultatai
    
    def pasalinti_remonta(self, remonto_id):
        self.cursor.execute('DELETE FROM remontai WHERE remonto_id = ?', (remonto_id,))
        self.conn.commit()

    def apskaiciuoti_vieno_automobilio_remontu_kaina(self, kliento_id, automobilio_id):
        self.cursor.execute(f'Select SUM(darbo_kaina) FROM remontai JOIN automobiliai ON remontai.kliento_id = automobiliai.kliento_id WHERE remontai.kliento_id = {kliento_id} AND automobiliai.automobilio_id = {automobilio_id}')
        rezultatai = self.cursor.fetchall()
        print(rezultatai)
        return rezultatai

    def apskaiciuoti_mechaniko_alga(self, mechaniko_id):
        self.cursor.execute(f'SELECT SUM(darbo_kaina) FROM remontai WHERE mechaniko_id = ?', (mechaniko_id,))
        rezultatai = self.cursor.fetchall()
        print('Jūsų pasirinkto mechaniko alga: ')
        print(rezultatai[0])
        return rezultatai
    
    def ar_yra_laisvu_mechaniku(self, darbo_pradzia, darbo_pabaiga, mechaniko_id):
        # print(f'SELECT * FROM remontai WHERE mechaniko_id = {mechaniko_id} AND (darbo_pradzia BETWEEN "{darbo_pradzia}" AND "{darbo_pabaiga}") AND (darbo_pabaiga BETWEEN "{darbo_pradzia}" AND "{darbo_pabaiga}")')
        # self.cursor.execute(f'SELECT * FROM remontai WHERE mechaniko_id = {mechaniko_id} AND (darbo_pradzia BETWEEN "{darbo_pradzia}" AND "{darbo_pabaiga}") AND (darbo_pabaiga BETWEEN "{darbo_pradzia}" AND "{darbo_pabaiga}")')
        self.cursor.execute(f'SELECT mechaniko_id FROM remontai WHERE mechaniko_id NOT IN (SELECT mechaniko_id FROM remontai WHERE (darbo_pradzia <= "{darbo_pabaiga}" AND darbo_pabaiga >= "{darbo_pradzia}"))')
        rezultatai = self.cursor.fetchall()
        print(rezultatai)