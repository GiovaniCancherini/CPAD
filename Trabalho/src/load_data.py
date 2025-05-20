import os
import pandas as pd

def load_all_data(path=None):
    if path is None:
        # Caminho absoluto da pasta data, a partir do src
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    dfs = []
    for year in range(2017, 2021):
        file_path = os.path.join(path, f'pda-prouni-{year}.csv')
        
        try:
            df = pd.read_csv(file_path, sep=';', encoding='utf-8-sig')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, sep=';', encoding='latin1')
            
        df['ANO_CONCESSAO_BOLSA'] = year
        dfs.append(df)

    return pd.concat(dfs, ignore_index=True)
