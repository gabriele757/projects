import sqlite3


# 1. sukurkite duomenų bazę, kurioje turėtų būti šios lentelės: gydytojai, pacientai, susitikimai

conn = sqlite3.connect('duomenu_baze_uzdaviniai.db')
cursor = conn.cursor()

# 1. Gydytojai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Specializacija
    # Kontaktinė informacija (el. paštas)

cursor.execute('''CREATE TABLE IF NOT EXISTS gydytojai
                (id INTEGER PRIMARY KEY,
                vardas VARCHAR(50) NOT NULL,
                pavarde VARCHAR(50) NOT NULL,
                specializacija VARCHAR(50) NOT NULL,
                kontaktine_informacija TEXT)''')

# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Elena', 'Petrovaite','Neurologija','elena.petrovaite@neurologai.lt'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Jonas', 'Kazlauskas','Chirurgija','jonas.kazlauskas@chirurgai.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Jurgita', 'Balciuniene','Traumatologija','jurgita.balciuniene@traumatologai.lt'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Algirdas', 'Navickas','Kardiologija','algirdas.navickas@kardiologai.comm'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Rasa', 'Maciuliene','Ginekologija','jrasa.maciuliene@ginekologai.lt'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Tomas', 'Juskevicius','Ortopedija','tomas.juskevicius@ortopedai.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Inga', 'Stankeviciute','Dermatologija','inga.stankeviciute@dermatologai.lt'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Mantas', 'Petrauskas','Chirurgija','mantas.petrauskas@chirurgai.lt'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Gintare', 'Petraitiene','Kardiologija','jgintare.petraitiene@kardiologai.com'))
# cursor.execute("INSERT INTO gydytojai (vardas, pavarde, specializacija, kontaktine_informacija) VALUES (?, ?, ?, ?)", ('Laura', 'Vaitiekunaite','Traumatologija','laura.vaitiekunaite@traumatologai.com'))

# cursor.execute("SELECT * FROM gydytojai")
# gydytojai = cursor.fetchall()
# print(type(gydytojai))
# for gydytojas in gydytojai:
#     print(gydytojas)
# print('------------------')

# 2. Pacientai:
    # ID (unikalus)
    # Vardas
    # Pavardė
    # Gimimo data
    # Lytis
    # Kontaktinė informacija (el. paštas)
    # Gydytojo ID (susiejimas su gydytoju, pvz. šeimos gydytojas)

cursor.execute('''CREATE TABLE IF NOT EXISTS pacientai
                (id INTEGER PRIMARY KEY,
                vardas VARCHAR(50) NOT NULL,
                pavarde VARCHAR(50) NOT NULL,
                gimimo_data DATE,
                lytis VARCHAR(50) NOT NULL,
                kontaktine_informacija TEXT,
                gydytojo_id INTEGER,
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai(gydytojo_id))''')

# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Jonas', 'Petrauskas','1985-03-12','Vyras', 'jonas.petrauskas@email.com', 7))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ("Laura", "Kazlauskienė", '1990-07-25', "Moteris", "laura.kazlauskiene@email.com", 3))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ("Andrius", "Jankauskas", '1978-11-05', "Vyras", "andrius.jankauskas@email.com", 9))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ("Rūta",  "Žvirblytė", '1982-09-18', "Moteris", "ruta.zvirblyte@email.com", 5))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Mantas', 'Rudys','1995-05-30','Vyras', "mantas.rudys@email.com", 2))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Gabija', 'Liutkute','1985-03-12','Moteris', 'gabija.liutkute@email.com', 8))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Tomas', 'Vaiciulis','1985-03-12','Vyras', 'tomas.vaiciulis@email.com', 6))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Ieva', 'Petrauskaite','1985-03-12','Moteris', 'ieva.petrauskaite@email.com', 1))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Simas', 'Gudelis','1985-03-12','Vyras', 'simas.gudelis@email.com', 10))
# cursor.execute("INSERT INTO pacientai (vardas, pavarde, gimimo_data, lytis, kontaktine_informacija, gydytojo_id) VALUES (?, ?, ?, ?, ?, ?)", ('Inga', 'Petrauskinene','1985-03-12','Moteris', 'inga.petrauskiene@email.com', 4))

# cursor.execute("SELECT * FROM pacientai")
# pacientai = cursor.fetchall()
# print(type(pacientai))
# for pacientas in pacientai:
#     print(pacientas)
# print('------------------')

# 3. Susitikimai:
    # ID
    # Paciento ID
    # Gydytojo ID
    # Susitikimo data ir laikas
    # Susitikimo paskirtis/arba diagnozė
    # Komentarai/arba pastabos

cursor.execute('''CREATE TABLE IF NOT EXISTS susitikimai
                (id INTEGER PRIMARY KEY,
                paciento_id INTEGER,
                gydytojo_id INTEGER,
                susitikimo_data DATE,
                susitikimo_paskirtis TEXT,
                komentarai TEXT,
                FOREIGN KEY (gydytojo_id) REFERENCES gydytojai (gydytojo_id)
                FOREIGN KEY (paciento_id) REFERENCES pacientai (paciento_id))''')

# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (5, 7, '2024-03-15 10:30:00', 'Įprastas konsultacijos vizitas', 'Pacientas skundziasi del miego sutrikimu'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (3, 9, '2023-09-18 15:45:00', 'Konsultacija del traumos', 'Aptarti rezultatai po kojos operacijos'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (8, 2, '2024-01-27 11:30:00', 'Operacijos aptarimas', 'Pacientas vis dar skundziasi skausmu kojos'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (6, 4, '2023-06-15 09:00:00', 'Įprastas konsultacijos vizitas', 'Nera'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (1, 10, '2024-02-01 10:30:00', 'Vizitas - galima rankos trauma', 'Israsyti vaistai nuo skausmo, paskirta operacija'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (9, 5, '2023-10-17 17:15:00', 'Rutinine apziura', 'Nera'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (2, 1, '2024-01-04 16:30:00', 'Vaistu recepto paruosimas', 'Israsytas receptas 3 menesiams'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (4, 8, '2023-06-15 15:00:00', 'Skubi konsultacija del operacijos', 'Paskirta operacijos data'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (10,6, '2023-11-05 08:45:00', 'Skubi konsultacija', 'Nera'))
# cursor.execute("INSERT INTO susitikimai (paciento_id, gydytojo_id, susitikimo_data, susitikimo_paskirtis, komentarai) VALUES (?, ?, ?, ?, ?)", (7, 3, '2023-09-25 13:15:00', 'Konsultacija del kojos (galima trauma)', 'Pakartotine kojos trauma, aptarta del operacijos'))

# cursor.execute("SELECT * FROM susitikimai")
# susitikimai = cursor.fetchall()
# print(type(susitikimai))
# for susitikimas in susitikimai:
#     print(susitikimas)
# print('------------------')

# 2. Užpildykite šias lenteles duomenimis (bent 10 įrašų kiekvienai lentelei)

# 3. Atlikite šias užklausas:

# cursor.execute('UPDATE pacientai SET gimimo_data = ? WHERE vardas = ?', ('1968-11-15', 'Laura'))
# cursor.execute("SELECT * FROM pacientai")
# pacientai = cursor.fetchall()
# print(type(pacientai))
# for pacientas in pacientai:
#     print(pacientas)

# 1. Visi pacientai, kurių gimimo data yra mažiau nei 1970-01-01 turėtų būti priskirti
    #  gydytojui, kurio ID yra 1

cursor.execute('UPDATE pacientai SET gydytojo_id = ? WHERE gimimo_data < ?', (1, '1970-01-01'))
try:
    cursor.execute("SELECT * FROM pacientai")
    conn.commit()
    print('Viskas pavyko')
except Exception as e:
    conn.rollback()
    print('Transakcija atsaukta', e)
finally:
    conn.close()

conn = sqlite3.connect('duomenu_baze_uzdaviniai.db')
cursor  = conn.cursor()

cursor.execute('SELECT * FROM pacientai')
pacientai = cursor.fetchall()
print ('-----------------------')
for pacientas in pacientai:
    print(pacientas)

 # 2. Raskite visus susitikimus, kurie vyksta šiandien. (rezultate norime matyti 
    # kliento vardą ir pavardę, gydytojo vardą ir pavardę ir susitikimo paskirtį)

cursor.execute('UPDATE susitikimai SET susitikimo_data = ? WHERE gydytojo_id = ?', ('2024-05-08 14:30:00', '5'))
cursor.execute("SELECT * FROM susitikimai")
susitikimai = cursor.fetchall()

for susitikimas in susitikimai:
    print(susitikimas)

cursor.execute('''SELECT pacientai.vardas, pacientai.pavarde, gydytojai.vardas, gydytojai.pavarde, susitikimo_paskirtis FROM susitikimai JOIN pacientai ON pacientai.id = susitikimai.paciento_id JOIN gydytojai ON gydytojai.id = pacientai.gydytojo_id WHERE susitikimo_data LIKE "2024-05-08%"''')
susitikimu_data = cursor.fetchall()
print ('-----------------------')
for susitikimas in susitikimu_data:
    print(susitikimas)

cursor.execute('UPDATE susitikimai SET susitikimo_data = ? WHERE gydytojo_id = ?', ('2024-05-08 11:15:00', '7'))
cursor.execute("SELECT * FROM susitikimai")
susitikimai = cursor.fetchall()
print ('-----------------------')
for susitikimas in susitikimai:
    print(susitikimas)

# 3. Sukurkite užklausą, kuri ištrintų visus susitikimus, kurie įvyko daugiau nei 6 
    # mėnesiai nuo šiandienos datos.

cursor.execute('DELETE FROM susitikimai WHERE susitikimo_data < "2023-11-08"')
susitikimai = cursor.fetchall()
for susitikimas in susitikimai:
    print(susitikimas)


# 4. Parašykite užklausą, kuri rastų gydytojų vardus ir pavardes, kuriems yra 
    # priskirti pacientai, kurių susitikimo paskirtyje yra žodis "trauma"

cursor.execute('SELECT gydytojai.vardas, gydytojai.pavarde FROM susitikimai JOIN gydytojai ON susitikimai.gydytojo_id = gydytojai.id WHERE susitikimo_paskirtis LIKE "%trauma%"')
rezultatas = cursor.fetchall()
print ('-----------------------')
for info in rezultatas:
    print(info)


# 5. Raskite visus pacientus, kurių gydytojo specializacija yra chirurgija ir 
    # susitikimo paskirtis yra operacija.

try:
    cursor.execute('SELECT * FROM susitikimai LEFT JOIN gydytojai ON gydytojai.id = susitikimai.gydytojo_id WHERE gydytojai.specializacija LIKE ("chirurgija") AND susitikimai.susitikimo_paskirtis LIKE "%operac%" ')
    rezultatas = cursor.fetchall()
    print ('-----------------------')
    for info in rezultatas:
        print(info)
except Exception as e:
    print('Kazkas negerai: ', e)

conn.commit()
conn.close()
