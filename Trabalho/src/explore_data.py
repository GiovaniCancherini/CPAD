def summarize(df):
    summary = {
        'Total registros': len(df),
        'Atributos': list(df.columns),
        'Dados faltantes (%)': df.isnull().mean() * 100,
        'Tipos de dados': df.dtypes,
        'Estatísticas numéricas': df.describe(include='number'),
        'Estatísticas categóricas': df.describe(include='object')
    }
    return summary
