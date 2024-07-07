import sqlite3

# prisijungiame prie duomenu bazes
conn = sqlite3.connect('duomenu_baze.db')

#sukuriame objekta, kuris leis  vykdyti uzduotis

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS zmones
#                (id INTEGER PRIMARY KEY,
#                vardas TEXT,
#                amzius INTEGER)''')

# '''SELECT * FROM preke WHERE description LIKE "%stalas%"'''

# cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES (?, ?)", ('Jonas', 30))
# cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES (?, ?)", ('Petras', 40))
# cursor.execute("INSERT INTO zmones (vardas, amzius) VALUES (?, ?)", ('Ona', 20))

# cursor.execute("SELECT * FROM zmones")
# rezultatai = cursor.fetchall()
# print(type(rezultatai))
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute("SELECT * FROM zmones WHERE amzius > 25")
# rezultatai = cursor.fetchall()
# print('-------------------')
# for zmogus in rezultatai:
#     print(zmogus)

# # tokia pati uzklausa, tik yra naudojami kintamieji
# amzius =  25
# cursor.execute(f"SELECT  * FROM zmones WHERE amzius > {amzius}")
# rezultatai = cursor.fetchall()
# print('-----------------')
# for zmogus in rezultatai:
#     print(zmogus)

# # vel tas  pats, taciau dazniau naudojamas butent su uzklausomis
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('-----------------')
# for zmogus in rezultatai:
#     print(zmogus)

# cursor.execute('UPDATE zmones SET amzius = ? WHERE vardas = ?', (31, 'Jonas'))
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('-----------------')
# for zmogus in rezultatai:
#     print(zmogus)

# ka_istrinti = input('Iveskite varda, kuri norite istrinti: ')
# cursor.execute('DELETE FROM zmones WHERE vardas = ?', (ka_istrinti,))
# cursor.execute(f'DELETE FROM  zmones WHERE vardas = {ka_istrinti}')

# cursor.execute('UPDATE zmones SET amzius = ? WHERE vardas = ?', (31, 'Jonas'))
# cursor.execute(f"SELECT * FROM zmones WHERE amzius > ?", (25,))
# rezultatai = cursor.fetchall()
# print('-----------------')
# for zmogus in rezultatai:
#     print(zmogus)


# 'SELECT * FROM prekes'

# 'SELECT * FROM prekes WHERE category = "turistines prekes"'

cursor.execute("""
    CREATE TABLE IF NOT EXISTS klientai (
               kliento_id INTEGER PRIMARY KEY,
               vardas VARCHAR(50) NOT NULL,
               pavarde VARCHAR(50) NOT NULL,
               el_pastas TEXT)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS prekes (
               prekes_id INTEGER PRIMARY KEY,
               pavadinimas TEXT NOT NULL,
               kaina REAL)""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS uzsakymai (
               uzsakymo_id INTEGER PRIMARY KEY,
               kliento_id INTEGER,
               prekes_id INTEGER,
               kiekis INTEGER,
               FOREIGN KEY (kliento_id) REFERENCES klientai(kliento_id),
               FOREIGN KEY (prekes_id) REFERENCES prekes(prekes_id))""")


# cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)", ('Jonas','Jonaitis','jonas@jonaitis.com'))
# cursor.execute("INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)", ('Petras','Petraitis','petras@petraitis.com'))

# cursor.execute("INSERT INTO prekes (pavadinimas, kaina) VALUES (?, ?)", ('Kava', 9.99))
# cursor.execute("INSERT INTO prekes (pavadinimas, kaina) VALUES (?, ?)", ('Arbata', 4.99))

# cursor.execute("INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?, ?, ?)", (1, 1, 2))
# cursor.execute("INSERT INTO uzsakymai (kliento_id, prekes_id, kiekis) VALUES (?, ?, ?)", (2, 2, 5))

cursor.execute('SELECT * FROM uzsakymai')
uzsakymai = cursor.fetchall()
for uzsakymas in uzsakymai:
    print(uzsakymas)

cursor.execute('SELECT uzsakymo_id, vardas, pavarde, pavadinimas, kiekis FROM uzsakymai JOIN klientai ON klientai.kliento_id = uzsakymai.kliento_id JOIN prekes ON uzsakymai.prekes_id = prekes.prekes_id')
uzsakymai_kliento_data = cursor.fetchall()
for uzsakymas in uzsakymai_kliento_data:
    print(uzsakymas)

# cursor.execute('DESCRIBE klientai')
# rezultatas = cursor.fetchall()
# print(rezultatas)

try:
    cursor.execute('BEGIN TRANSACTION')
    cursor.execute('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)', ('Romas', 'Tomaitis', 'antanas@antanaitis.com'))
    cursor.execute('UPDATE klientai SET el_pastas2 = ? WHERE kliento_id = ?', ('antanas@gmail.com', 3))
    conn.commit()
    print('Viskas pavyko')
except Exception as e:
    conn.rollback()
    print('Transakcija atsaukta', e)
finally:
    conn.close()

conn = sqlite3.connect('duomenu_baze.db')
cursor  = conn.cursor() # antra karta sukuriam/initialiazinam kursoriu, nes pries tai buves yra susijes su sesija, kuri jau yra uzdaryta 
cursor.execute('SELECT * FROM klientai')
klientai = cursor.fetchall()
for klientas in klientai:
    print(klientas)


nauji_klientai = [
    ('Juozas','Juozaitis','juozas@juozaitis.com'),
    ('Kazys','Kaziauskas', 'kazys@kaziauskas.com')
]

cursor.executemany('INSERT INTO klientai (vardas, pavarde, el_pastas) VALUES (?, ?, ?)', nauji_klientai)

cursor.execute('SELECT * FROM klientai')
klientai = cursor.fetchall()
for klientas in klientai:
    print(klientas)

naujos_prekes = [
    ('Medus', 5),
    ('Batonas', 3)
]

cursor.executemany('INSERT INTO prekes (pavadinimas,kaina) VALUES (?, ?)', naujos_prekes)

cursor.execute('SELECT * FROM prekes')
prekes = cursor.fetchall()
for preke in prekes:
    print(preke)

conn.commit()
conn.close()