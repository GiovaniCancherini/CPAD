import pandas as pd
import os

def load_all_data(path='data/'):
    dfs = []
    for year in range(2017, 2021):
        file_path = os.path.join(path, f'prouni_{year}.csv')
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
        df['ANO_CONCESSAO_BOLSA'] = year  # garantir consistencia
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
