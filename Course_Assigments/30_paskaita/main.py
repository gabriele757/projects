from parduotuve import Preke, Parduotuve

parduotuve = Parduotuve()
failo_kelias = 'prekes.txt'

def pasirinkimai():
    print()
    print('Pasirinkite veiksmą:')
    print('1 - baigti darbą')
    print('2 - peržiūrėti prekes')
    print('3 - pridėti prekę')
    print('4 - nuskaityti failą')
    print('5 - pašalinti prekę')
    print('6 - gauti surikiuotas prekes')
    print('7 - atnaujinti prekę')
    print()

def prideti_preke():
    try:
        pavadinimas = input('Įveskite prekės pavadinimą: ')
        kaina = float(input('Įveskite kainą: '))
        kiekis = int(input('Įveskite keikį: '))
        nauja_preke = Preke(pavadinimas, kaina, kiekis)
        parduotuve.prideti_preke(nauja_preke)
        print(f'{pavadinimas} prekė pridėta sekmingai!')
        with open('prekes.txt', 'a+') as failas:
            failas.write(f'{pavadinimas} {kaina} {kiekis} \n')
    except Exception as e:
        print(f'Klaida:{e}')

def nuskaityti_faila(failo_pavadinimas):
    prekes = []
    try:
        with open(failo_pavadinimas, 'r') as failas:
            eilutes = failas.readlines()
            for eilute in eilutes:
                pavadinimas, kaina, kiekis = eilute.replace('\n', '').split()
                preke = Preke(pavadinimas, kaina, kiekis)
                prekes.append(preke)
                parduotuve.prideti_preke(preke)
        print('Prekės pridėtos sėkmingai!')
    except Exception as e:
        print(f'Klaida:{e}')

def pasalinti_preke():
    print()
    parduotuve.perziureti_prekes()
    print()
    istrinti = input('Įveskite index prekės, kurią norite ištrinti: ')
    try:
        parduotuve.istrinti_preke(istrinti)
        with open(failo_kelias, 'r') as failas:
            eilutes = failas.readlines()
        del eilutes[int(istrinti)]
        with open(failo_kelias, 'w') as failas:
            failas.writelines(eilutes)
        print('Prekė panaikinta sėkmingai')
    except Exception as e:
        print(f'Klaida:{e}')

def gauti_surikiuotas_prekes():
    rikiuoti_pagal = input('Įveskite pagal ką norite rikiuoti (pavadinimas/kaina/kiekis):  ')
    while rikiuoti_pagal not in ('pavadinimas','kaina','kiekis'):
        rikiuoti_pagal = input('Klaida! Įveskite pagal ką norite rikiuoti (pavadinimas/kaina/kiekis): ').lower
    rikiuotos_prekes = parduotuve.rikiuoti_pagal_savybe(rikiuoti_pagal)
    print(rikiuotos_prekes)

def atnaujinti_preke():
    print()
    parduotuve.perziureti_prekes()
    print()
    atnaujinti = int(input('Įveskite index prekės, kurią norite atnaujinti: '))
    try:
        pavadinimas = input('Įveskite naują prekės pavadinimą: ')
        kaina = float(input('Įveskite naują kainą: '))
        kiekis = int(input('Įveskite naują kiekį: '))
        nauja_preke = Preke(pavadinimas, kaina, kiekis)
        parduotuve.atnaujinti_preke(atnaujinti, nauja_preke)
        with open(failo_kelias, 'r') as failas:
            eilutes = failas.readlines()
        eilutes[atnaujinti] = f'{pavadinimas} {kaina} {kiekis} \n'
        with open(failo_kelias, 'w') as failas:
            failas.writelines(eilutes)
    except Exception as e:
        print(f'Klaida:{e}')


while True:
    pasirinkimai()
    pasirinkimas = input('Įveskite pasirinkimą: ')
    if pasirinkimas == '1':
        print('Programos pabaiga.')
        break
    elif pasirinkimas == '2':
        parduotuve.perziureti_prekes()
    elif pasirinkimas == '3':
        prideti_preke()
    elif  pasirinkimas == '4':
        if parduotuve.nuskaitytas:
            print('Failas jau buvo nuskaitytas!')
        else:
            failas = 'prekes.txt'
            nuskaityti_faila(failas)
            parduotuve.nuskaitytas = True
    elif pasirinkimas == '5':
        pasalinti_preke()
    elif pasirinkimas == '6':
        gauti_surikiuotas_prekes()
    elif pasirinkimas == '7':
        atnaujinti_preke()
    else:
        print('Pasirinkimas netinkamas, kartokite.')
