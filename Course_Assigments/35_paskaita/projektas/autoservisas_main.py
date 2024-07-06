from autoservisas import Autoservisas
from datetime import datetime

def main():

    autoservisas = Autoservisas()

    while True:
        print('\nPasirinkite veiksmą:')
        print('1 - baigti darbą')
        print('2 - pridėti mechaniką')
        print('3 - pridėti klientą')
        print('4 - pridėti kliento automobilį')
        print('5 - pridėti remontą')
        print('6 - peržiūrėti įrašus')
        print('7 - peržiūrėti visų kliento remontų sumą')
        print('8 - pašalinti remontą')
        print('9 - peržiūrėti vieno kliento automobilio remontų sumą')
        print('10 - peržiūrėti vieno mechaniko algą')
        pasirinkimas = input('Įveskite pasirinkimo numerį: ')

        if pasirinkimas == '1':
            print('\nProgramos pabaiga.\n')
            break
        elif pasirinkimas == '2':
            print('Įveskite mechaniko informaciją')
            vardas = input('Vardas: ')
            pavarde = input('Pavardė: ')
            el_pastas = input('El paštas: ')
            valandinis_atlyginimas = int(input('Valandinis atlyginimas: '))
            specializacija = input('Specializacija: ')
            mechanikas = autoservisas.prideti_mechanika(vardas, pavarde, el_pastas, valandinis_atlyginimas, specializacija)
            print()
            print(f'Mechanikas {mechanikas.vardas} buvo pridėtas sėkmingai !')
        elif pasirinkimas == '3':
            print('Įveskite kliento informaciją')
            vardas = input('Vardas: ')
            pavarde = input('Pavardė: ')
            el_pastas = input('El paštas: ')
            klientas = autoservisas.prideti_klienta(vardas, pavarde, el_pastas)
            print()
            print(f'Klientas(-ė) {klientas.vardas} buvo pridėtas(-a) sėkmingai !')
        elif pasirinkimas == '4':
            print('Įveskite automobilio informaciją')
            valstybinis_numeris = input('Valstybinis numeris: ')
            marke = input('Marke: ')
            modelis = input('Modelis: ')
            kliento_id = int(input('Kliento_id: '))
            automobilis = autoservisas.prideti_automobili(valstybinis_numeris, marke, modelis, kliento_id)
            print()
            print(f'Automobilis {automobilis.marke} {automobilis.modelis} buvo pridėtas(-a) sėkmingai !')
        elif pasirinkimas == '5':
            print('Įveskite informaciją apie remontą')
            kliento_id = int(input('Kliento_id: '))
            mechaniko_id = int(input('Mechaniko_id: '))
            darbo_pradzia = input('Darbo pradžios data: ')
            darbo_pabaiga = input('Darbo pabaigos data: ')
            remonto_kategorija = input('Remonto kategorija: ')
            remontas = autoservisas.prideti_remonta(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija)
            if autoservisas.ar_yra_laisvu_mechaniku(darbo_pradzia, darbo_pabaiga, kliento_id):
                remontas = autoservisas.prideti_remonta(kliento_id, mechaniko_id, darbo_pradzia, darbo_pabaiga, remonto_kategorija)
                print(f'Remontas pridėtas sėkmingai !')
            else:
                print('Remonto pridėti nepavyko, Jūsų nurodytu laiku nėra laisvų mechanikų.')
            # print()
            # print(f'Remontas pridėtas sėkmingai !')
        elif pasirinkimas == '6':
            lentele = input('Kokios (mechanikai/klientai/automobiliai/remontai) lentelės įrašus norite peržiūrėti: ')
            while lentele not in ['mechanikai','klientai','automobiliai','remontai']:
                print('Pasirinkimas neteisingas, bandykite dar kartą')
                lentele = input('Kokios (mechanikai/klientai/automobiliai/remontai) lentelės įrašus norite peržiūrėti: ')
            autoservisas.perziureti_irasus(lentele)
        elif pasirinkimas == '7':
            kliento_id = input('Kokio kliento sumą už visus remontus norite peržiūrėti? Įrašykite id: ')
            while kliento_id not in ['1','2','3']:
                print('Pasirinkimas neteisingas, bandykite dar kartą')
                kliento_id = input('Kokio kliento sumą už visus remontus norite peržiūrėti? Įrašykite id: ')
            autoservisas.apskaiciuoti_visus_remontus_pagal_kliento_id(kliento_id)
        elif pasirinkimas == '8':
            print('Įveskite id remonto, kurį norite pašalinti')
            remonto_id  = int(input('Remonto id: '))
            autoservisas.pasalinti_remonta(remonto_id)
            print()
            print(f'Remontas pašalintas sėkmingai !')
        elif pasirinkimas == '9':
            kliento_id = input('Kokio kliento remontus norite peržiūrėti? Įrašykite id: ')
            automobilio_id = input('Kokio automobilio remontų sumą norite peržiūrėti? Įrašykite id: ')
            while kliento_id not in ['1','2','3'] or automobilio_id not in ['1', '2', '3']:
                print('Pasirinkimas neteisingas, bandykite dar kartą')
                kliento_id = input('Kokio kliento remontus norite peržiūrėti? Įrašykite id: ')
                automobilio_id = input('Kokio automobilio remontų sumą norite peržiūrėti? Įrašykite id: ')
            autoservisas.apskaiciuoti_vieno_automobilio_remontu_kaina(kliento_id, automobilio_id)
        elif pasirinkimas == '10':
            print('Įveskite mechaniko id, kurio algą norite peržiūrėti: ')
            mechaniko_id = int(input('Mechaniko id: '))
            autoservisas.apskaiciuoti_mechaniko_alga(mechaniko_id)
            print()
        else:
            print('Pasirinkimas neteisingas, bandykite dar kartą')

if __name__ == '__main__':
    main()