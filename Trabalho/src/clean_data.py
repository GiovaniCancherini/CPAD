import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip().str.upper()
    
    df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'], errors='coerce', dayfirst=True)

    if 'CPF_BENEFICIARIO' in df.columns:
        df.drop(columns=['CPF_BENEFICIARIO'], inplace=True)
    
    cat_cols = ['SEXO_BENEFICIARIO', 'RACA_BENEFICIARIO', 'TIPO_BOLSA',
                'MODALIDADE_ENSINO_BOLSA', 'NOME_TURNO_CURSO_BOLSA']
    
    for col in cat_cols:
        df[col] = df[col].str.strip().str.capitalize()

    return df
