# Trabalho Extensionista 

##  Análise de Bolsas Prouni (2017–2020)

Este projeto analisa os dados de concessão de bolsas do Prouni de 2017 a 2020 para investigar possíveis mudanças no perfil dos alunos beneficiados, com foco no impacto da pandemia em 2020.


## Etapas
- Carregamento e unificação dos dados
- Limpeza e pré-processamento
- Análise exploratória
- Visualizações comparativas


## Instalando ambiente de Desenvolvimento (venv)
```sh
python -m pip install --upgrade pip # atualizar pip

python -m venv cpad-venv            # criar ambiente venv
cpad-venv\Scripts\activate          # ativar ambiente
deactivate                          # desativar ambiente
```
### Instalando requisitos
```sh
pip install -r requirements.txt     # instalar requisitos
```

## Requisitos
- Python 3.12+
- Pandas, Matplotlib, Seaborn
### Instalando requisitos
```sh
pip install -r requirements.txt
```


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