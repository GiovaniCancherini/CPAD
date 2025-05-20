# Trabalho Extensionista 





## Estrutura
```
prouni_analysis/
│
├── data/                      # Arquivos CSV originais
│   ├── prouni_2017.csv
│   ├── prouni_2018.csv
│   ├── prouni_2019.csv
│   └── prouni_2020.csv
│
├── notebooks/                 # Análises e visualizações interativas
│   ├── 01_data_understanding.ipynb
│   └── 02_data_preparation.ipynb
│
├── src/                       # Código Python reutilizável
│   ├── __init__.py
│   ├── load_data.py
│   ├── clean_data.py
│   ├── explore_data.py
│   └── utils.py
│
├── outputs/                   # Figuras, gráficos e tabelas exportadas
│
├── README.md                  # Breve descrição do projeto
└── requirements.txt           # Dependências

```