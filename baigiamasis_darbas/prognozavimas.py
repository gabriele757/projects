import pandas as pd
from joblib import load
import sqlite3

# susikuriam ir apibūdinam klasę
class WinRatePrognozavimas:
    def __init__(self, model_path='best_model.joblib', data_path='lol_champions_data_updated.csv', db_path='prognozavimas.db'):
        # paleidžiam apmokytą modelį
        self.model = load(model_path)
        # nuskaitom failą, kuriame yra informacija apie žaidėjus
        self.data = pd.read_csv(data_path)
        # sugrupuojam duomenis pagal champion id
        self.champion_data = self.data.groupby('Champion ID').first().reset_index()
        # prisijungiam prie sqlite duonbazes
        self.db_conn = sqlite3.connect(db_path)
        self.create_table()
    
    # sukuriam lentelę duonbazėje
    def create_table(self):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS spejimai (
                ID INTEGER PRIMARY KEY,
                RankID INT,
                RegionID INT,
                RoleID INT,
                ChampionID INT,
                PredictedWinRate TEXT
            )
        ''')
        self.db_conn.commit()

    # susikuriam funkciją prognozuoti win rate
    def predict_win_rate(self, rank_id, region_id, role_id, champion_id):
        # filtruojam reikiamą informaciją pagal champion id
        champion_row = self.champion_data[self.champion_data['Champion ID'] == champion_id]
        
        if not champion_row.empty:
            champion_row = champion_row.iloc[0]
            # susikuriam žodyną features, kurie bus naudojami atliekant spėjimus
            features = {'Champion ID': champion_id, 'Rank ID': rank_id, 'Region ID': region_id, 'Pick Rate': champion_row['Pick Rate'], 'Ban Rate': champion_row['Ban Rate'], 'Matches': champion_row['Matches'], 'Role': role_id,
                'Worst Against 1': champion_row['Worst Against 1'], 'Worst Against 2': champion_row['Worst Against 2'], 'Worst Against 3': champion_row['Worst Against 3'], 'Worst Against 4': champion_row['Worst Against 4'], 
                'Worst Against 5': champion_row['Worst Against 5'],  'Worst Against 6': champion_row['Worst Against 6'], 'Best Against 1': champion_row['Best Against 1'], 'Best Against 2': champion_row['Best Against 2'], 
                'Best Against 3': champion_row['Best Against 3'], 'Best Against 4': champion_row['Best Against 4'], 'Best Against 5': champion_row['Best Against 5'], 'Best Against 6': champion_row['Best Against 6'],
                'Best With 1': champion_row['Best With 1'], 'Best With 2': champion_row['Best With 2'], 'Best With 3': champion_row['Best With 3'], 'Best With 4': champion_row['Best With 4'], 'Best With 5': champion_row['Best With 5'], 
                'Best With 6': champion_row['Best With 6'], 'Similar Champion 1': champion_row['Similar Champion 1'], 'Similar Champion 2': champion_row['Similar Champion 2'], 'Similar Champion 3': champion_row['Similar Champion 3'], 
                'Similar Champion 4': champion_row['Similar Champion 4'], 'WR Worst Against1': champion_row['WR Worst Against1'], 'WR Worst Against2': champion_row['WR Worst Against2'], 'WR Worst Against3': champion_row['WR Worst Against3'], 
                'WR Worst Against4': champion_row['WR Worst Against4'], 'WR Worst Against5': champion_row['WR Worst Against5'], 'WR Worst Against6': champion_row['WR Worst Against6'], 'WR Best Against1': champion_row['WR Best Against1'], 
                'WR Best Against2': champion_row['WR Best Against2'], 'WR Best Against3': champion_row['WR Best Against3'], 'WR Best Against4': champion_row['WR Best Against4'], 'WR Best Against5': champion_row['WR Best Against5'], 
                'WR Best Against6': champion_row['WR Best Against6'], 'WR Best With1': champion_row['WR Best With1'], 'WR Best With2': champion_row['WR Best With2'], 'WR Best With3': champion_row['WR Best With3'], 
                'WR Best With4': champion_row['WR Best With4'], 'WR Best With5': champion_row['WR Best With5'], 'WR Best With6': champion_row['WR Best With6']
            }
        else:
            print('Nerasta informacijos apie žaidėją.')
            return None
        
        features_df = pd.DataFrame([features])
        win_rate_prediction = self.model.predict(features_df)
        win_rate_prediction_value = win_rate_prediction[0]
        # susitvarkom formatą prediction
        win_rate_prediction_new = "{:.2f}%".format(win_rate_prediction_value)
        # visą informaciją išsaugom
        self.save_to_db(rank_id, region_id, role_id, champion_id, win_rate_prediction_new)
        # susikuriam sąrašus, kuriuos norėsim pateikti po user input (dėl papildomos informacijos)
        # prieš ką nerekomenduojama rinktis
        worst_against_ids = [
            champion_row['Worst Against 1'], champion_row['Worst Against 2'], champion_row['Worst Against 3'],
            champion_row['Worst Against 4'], champion_row['Worst Against 5'], champion_row['Worst Against 6']
        ]
        worst_against_champions = self.champion_data[self.champion_data['Champion ID'].isin(worst_against_ids)]
        worst_against = worst_against_champions['Champion Name'].tolist()
        # kada rekomenduojama rinktis
        best_against_ids = [
            champion_row['Best Against 1'], champion_row['Best Against 2'], champion_row['Best Against 3'],
            champion_row['Best Against 4'], champion_row['Best Against 5'], champion_row['Best Against 6']
        ]
        best_against_champions = self.champion_data[self.champion_data['Champion ID'].isin(best_against_ids)]
        best_against = best_against_champions['Champion Name'].tolist()
        best_with_ids = [
            champion_row['Best With 1'], champion_row['Best With 2'], champion_row['Best With 3'],
            champion_row['Best With 4'], champion_row['Best With 5'], champion_row['Best With 6']
        ]
        best_with_champions = self.champion_data[self.champion_data['Champion ID'].isin(best_with_ids)]
        best_with = best_with_champions['Champion Name'].tolist()

        # gražinam visus reikiamus duomenis
        return win_rate_prediction_new, worst_against, best_against, best_with
    
    # susikuriam funkciją surasti visus žaidėjus pagal role id
    def list_of_champions_by_role(self, role_id):
        champions_by_role = self.data[self.data['Role'] == role_id]
        # susitvarkom, kad nebūtų besidubliuojančių įrašų
        unikalus_champions = champions_by_role.drop_duplicates(subset = ['Champion ID'])
        print()
        print("Jūsų pasirinktos pozicijos žaidėjų sąrašas: ")
        print()
        for index, champion in unikalus_champions.iterrows(): # iteruojam per dataframe eilutes
            print(f"{champion['Champion ID']} - {champion['Champion Name']}")
        return unikalus_champions

    # susikuriam funkciją surasti visus žaidimo žaidėjus
    def list_of_all_champions(self):
        champions_list = self.champion_data[['Champion ID', 'Champion Name']].drop_duplicates()
        print('Visų žaidėjų sąrašas: ')
        for index, champion in champions_list.iterrows(): # iteruojam per dataframe eilutes
            print(f"{champion['Champion ID']} - {champion['Champion Name']}")

    # susikuriam funkciją peržiūrėti visus jau atliktus spėjimus
    def see_all_predictions(self):
        cursor = self.db_conn.cursor()
        cursor.execute('SELECT * FROM spejimai')
        predictions = cursor.fetchall()
        print("Visi atlikti spėjimai: ")
        print()
        print('RankID, RegionID, RoleID, ChampionID, PredictedWinRate')
        for prediction in predictions:
            print(prediction)

    # susikuriam funkcją ištrinti kurį nors spėjimą (pagal pasirinktą id)
    def delete_prediction(self, spejimo_id):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            DELETE FROM spejimai WHERE ID = ?
        ''', (spejimo_id,))
        self.db_conn.commit()
        print(f"Spėjimas (ID = {spejimo_id}) sėkmingai pašalintas !")

    # susikuriam funkciją išsaugoti duomenis į duonbazę
    def save_to_db(self, rank, region, role, champion_id, win_rate_prediction_new):
        cursor = self.db_conn.cursor()
        cursor.execute('''
            INSERT INTO spejimai (RankID, RegionID, RoleID, ChampionID, PredictedWinRate) 
            VALUES (?, ?, ?, ?, ?)
        ''', (rank, region, role, champion_id, win_rate_prediction_new))
        self.db_conn.commit()

    def __del__(self):
        self.db_conn.close()
