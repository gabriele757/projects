# Import necessary libraries
from prognozavimas import WinRatePrognozavimas

def main():

    win_rate_prognozavimas = WinRatePrognozavimas()

    # susikuriam pasirinkimų meniu
    while True:
        print('\nPasirinkite veiksmą:')
        print('1 - baigti darbą')
        print('2 - prognozuoti pasirinkto žaidėjo laimėjimo procentą')
        print('3 - peržiūrėti visų žaidėjų sąrašą')
        print('4 - peržiūrėti visus atliktus spėjimus')
        print('5 - pašalinti spėjimą')

        pasirinkimas = input('Įveskite pasirinkimo numerį: ')

        if pasirinkimas == '1':
            print('\nProgramos pabaiga.\n')
            break
        elif pasirinkimas == '2':
            rank_id = int(input("Pasirinkite diviziją (rank) (1 - Iron, 2- Bronze, 3 - Silver, 4 - Gold, 5 - Platinum, 6 - Emerald, 7 - Diamond, 8 - Master): "))
            region_id = int(input("Pasirinkite regioną (region) (1 - Korea, 2 - North America, 3 - Europe West, 4 - Eurone N&E, 5 - Brasil, 6 - LAN, 7 - Oceania, 8 - LAS, 9 - Philippines, 10 - Taiwan, 11 - Vietnam): "))
            role_id = int(input("Pasirinkit poziciją (role) (1 - Top, 2 - Mid, 3 - Jungle, 4 - Bot/Adc, 5 - Support ): "))
            champions_by_role_df = win_rate_prognozavimas.list_of_champions_by_role(role_id)
            while True:
                # useris pasirenka žaidėją iš sąrašo
                try:
                    champion_id = int(input("Pasirinkite žaidėją iš sąrašo: "))
                    # patikrinam ar pasirinktas žaidėjo id yra sąraše
                    if champion_id in champions_by_role_df['Champion ID'].values:
                        break
                    else:
                        print("Pasirinktas žaidėjas nepriklauso pasirinktai pozicijai. Bandykite dar kartą.")
                except ValueError:
                    print("Neteisingas pasirinkimas. Prašome įvesti tinkamą žaidėjo ID.")
            prediction, worst_against, best_against, best_with = win_rate_prognozavimas.predict_win_rate(rank_id, region_id, role_id, champion_id)
            print()
            print('Prognozuojamas laimėjimo procentas:', prediction)
            print()
            print('Jūsų nurodyto žaidėjo nerekomenduojama rinktis jeigu žaidžiate prieš: ', ' / '.join(worst_against))
            print()
            print('Jūsų nurodytą žaidėją rekomenduojama rinktis jeigu žaidžiate prieš: ', ' / '.join(best_against), '\n' 'ir/arba jeigu Jūsų komandoje yra: ', ' / '.join(best_with))
        elif pasirinkimas == '3':
            print()
            win_rate_prognozavimas.list_of_all_champions() # spausdina visų žaidėjų sąrašą
        elif pasirinkimas == '4':
            print()
            win_rate_prognozavimas.see_all_predictions() # parodo visus atliktus spėjimus
        elif pasirinkimas == '5':
            spejimo_id = int(input('Įveskite ID spėjimo, kurį norite pašalinti: '))
            print()
            win_rate_prognozavimas.delete_prediction(spejimo_id) # pašalina spėjimą pagal pasirinktą id
        else:
            print()
            print('Tokio pasirinkimo nėra. Bandykite dar kartą. ')

if __name__ == "__main__":
    main()
