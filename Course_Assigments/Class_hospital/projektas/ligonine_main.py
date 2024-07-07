from ligonine import Ligonine

def main():

    ligonine = Ligonine()

    while True:
        print('\nPasirinkite veiksmą:')
        print('1 - baigti darbą')
        print('2 - pridėti gydytoją')
        print('3 - pridėti pacientą')
        print('4 - pridėti susitikimą')
        print('5 - pašalinti gydytoją')
        print('6 - pašalinti pacientą')
        print('7 - pašalinti susitikimą')
        print('8 - peržiūrėti įrašus')

        pasirinkimas = input('Įveskite pasirinkimo numerį: ')

        if pasirinkimas == '1':
            print('\nProgramos pabaiga.\n')
            break
        elif pasirinkimas == '2':
            print('Įveskite gydytojo informaciją')
            vardas = input('Vardas: ')
            pavarde = input('Pavardė: ')
            specializacija = input('Specializacija: ')
            el_pastas = input('El_paštas: ')
            gydytojas = ligonine.prideti_gydytoja(vardas, pavarde, specializacija, el_pastas)
            print()
            print(f'Gydytojas(-a) {gydytojas.vardas} buvo pridėtas(-a) sėkmingai !')
        elif pasirinkimas == '3':
            print('Įveskite paciento informaciją')
            vardas = input('Vardas: ')
            pavarde = input('Pavardė: ')
            gimimo_data = input('Gimimo data: ')
            lytis = input('Lytis: ')
            el_pastas = input('El_paštas: ')
            gydytojo_id = int(input('Gydytojo id: '))
            pacientas = ligonine.prideti_pacienta(vardas, pavarde, gimimo_data, lytis, el_pastas, gydytojo_id)
            print()
            print(f'Pacientas(-ė) {pacientas.vardas} buvo pridėtas(-a) sėkmingai !')
        elif pasirinkimas == '4':
            print('Įveskite susitikimo informaciją')
            paciento_id = int(input('Paciento id: '))
            gydytojo_id = int(input('Gydytojo id: '))
            susitikimo_data = input('Susitikimo data: ')
            paskirtis = input('Paskirtis: ')
            komentarai = input('Komentarai: ')
            susitikimo_id = ligonine.prideti_susitikima(paciento_id, gydytojo_id, susitikimo_data, paskirtis, komentarai)
            susitikimas = ligonine.gauti_susitikimo_info_pagal_id(int(susitikimo_id))
            pac_vardas, gyd_vardas, data = susitikimas #unpack
            print(susitikimas)
            print()
            print(f'Paciento {pac_vardas} susitikimas su gydytoju {gyd_vardas} buvo pridėtas sėkmingai ! Vizito data: {data}')
        elif pasirinkimas == '5':
            gydytojo_id = int(input('Gydytojo id: '))
            pasalinimas = ligonine.pasalinti_gydytoja(gydytojo_id)
            print()
            print(f'Gydytojas buvo pašalintas sėkmingai !')
        elif pasirinkimas == '6':
            paciento_id = int(input('Paciento id: '))
            pasalinimas = ligonine.pasalinti_pacienta(paciento_id)
            print()
            print(f'Pacientas buvo pašalintas sėkmingai !')
        elif pasirinkimas == '7':
            susitikimo_id = int(input('Susitikimo id: '))
            pasalinimas = ligonine.pasalinti_susitikima(susitikimo_id)
            print()
            print(f'Susitikimas buvo pašalintas sėkmingai !')
        elif pasirinkimas == '8':
            lentele = input('Kokios (gydytojai/pacientai/susitikimai) lentelės įrašus norite peržiūrėti: ')
            while lentele not in ['gydytojai','pacientai','susitikiami']:
                print('Pasirinkimas neteisingas, bandykite dar kartą')
                lentele = input('Kokios (gydytojai/pacientai/susitikimai) lentelės įrašus norite peržiūrėti: ')
            ligonine.perziureti_irasus(lentele)    
        else:
            print('Pasirinkimas neteisingas, bandykite dar kartą')

if __name__ == '__main__':
    main()