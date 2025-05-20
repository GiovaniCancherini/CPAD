# 📊 Coleta, Preparação e Análise de Dados (CPAD)

## Projeto: Análise de Bolsas Prouni (2017–2020)

**Grupo:** Giovani Cancherini, Eduardo Traunig, Vinicius Quintian, João Pedro Fossa

Repositório central da disciplina *Coleta, Preparação e Análise de Dados* (CPAD), contendo aulas, exercícios avaliativos e o projeto final de análise de dados.

---

## 🧪 Ambiente de Desenvolvimento

### 🔹 Requisitos

- Python `3.12.5`
- Pip

### 📦 Instalação e Ativação

```sh
# Atualizar pip (opcional)
python -m pip install --upgrade pip

# Criar ambiente virtual
python -m venv cpad-venv

# Ativar ambiente virtual
cpad-venv\Scripts\activate        # Windows
# source cpad-venv/bin/activate   # Linux/macOS

# Instalar dependências do projeto
pip install -r requirements.txt
````

---

## 🧠 Projeto Principal

### 🎯 Título

**Análise do Impacto da Pandemia de COVID-19 no Perfil dos Beneficiários do Prouni (2017–2020)**

### 🔍 Problema

A pandemia de COVID-19 alterou o perfil dos beneficiários do Prouni? Houve impacto na distribuição das bolsas?

### 💡 Solução Proposta

Analisar os dados de concessão de bolsas entre 2017 e 2020 para identificar possíveis mudanças nos perfis dos beneficiários, considerando variáveis como sexo, raça, tipo de bolsa e modalidade de ensino.

---

## 📦 Entregas Planejadas

* ✅ Dataset unificado e limpo (2017–2020)
* 📊 Relatório de análise exploratória com estatísticas descritivas
* 📈 Visualizações comparativas entre os anos
* 📌 Conclusões baseadas nos impactos observados
* 📽️ Painel/apresentação final com principais achados

---

## 🔄 Metodologia: CRISP-DM

| Etapa               | Atividades Realizadas/Planejadas                                        | Progresso |
| ------------------- | ----------------------------------------------------------------------- | --------- |
| Data Understanding  | Análise de atributos, tipos, dados faltantes e estatísticas descritivas | 50%       |
| Data Preparation    | Limpeza, tratamento de nulos, padronização e unificação de datasets     | 20%       |
| Modeling (opcional) | \[Possível aplicação de clusterização ou regressão logística simples]   | 0%        |

---

## 📚 Atributos Relevantes

| Atributo                         | Tipo                   | Exemplo               |
| -------------------------------- | ---------------------- | --------------------- |
| ANO\_CONCESSAO\_BOLSA            | Numérico discreto      | 2020                  |
| NOME\_IES\_BOLSA                 | Categórico nominal     | UNIVERSIDADE PAULISTA |
| TIPO\_BOLSA                      | Categórico nominal     | INTEGRAL / PARCIAL    |
| MODALIDADE\_ENSINO\_BOLSA        | Categórico nominal     | PRESENCIAL / EAD      |
| SEXO\_BENEFICIARIO               | Categórico nominal     | M / F                 |
| RACA\_BENEFICIARIO               | Categórico nominal     | Parda / Branca / etc. |
| DATA\_NASCIMENTO                 | Data → Idade calculada | 11/08/1973            |
| BENEFICIARIO\_DEFICIENTE\_FISICO | Binário (Y/N)          | S / N                 |
| UF\_BENEFICIARIO                 | Categórico nominal     | MG / CE / etc.        |

---

## 📊 Estatísticas Preliminares

* Total de registros: `[a ser atualizado após unificação]`
* Faixa etária: Média, mínimo, máximo, desvio padrão
* Distribuição por sexo, tipo de bolsa e modalidade ao longo dos anos

---

## 🧹 Planejamento de Pré-Processamento

| Etapa                        | Ação                                                             |
| ---------------------------- | ---------------------------------------------------------------- |
| Remoção de atributos         | Excluir `CPF_BENEFICIARIO`                                       |
| Conversão de atributos       | `DATA_NASCIMENTO` → `IDADE`                                      |
| Tratamento de nulos          | Preencher `RACA` com "Não Informado", `SEXO` com moda ou excluir |
| Normalização de categorias   | Padronizar strings (acentuação, espaços, maiúsculas)             |
| Agrupamento por faixa etária | Ex.: "18-25", "26-35", etc.                                      |
| Filtro de anos               | Considerar apenas registros entre 2017 e 2020                    |
| Unificação de datasets       | Concatenar arquivos anuais em um único DataFrame                 |

---

## 🛠️ Ferramentas e Bibliotecas

* [`pandas`](https://pandas.pydata.org/)
* [`matplotlib`](https://matplotlib.org/)
* [`seaborn`](https://seaborn.pydata.org/)
* [`jupyter`](https://jupyter.org/)
* [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) (se necessário para scraping)

---

## 📌 Observações

* O projeto busca aplicar técnicas de análise exploratória, pré-processamento e visualização de dados.
* Os scripts e notebooks estão organizados nas respectivas pastas (`TRABALHO`, `AULAS`, `EXx`).
* A apresentação final deverá destacar os principais achados e aprendizados do grupo.

---

## 📬 Contato

Disciplina: *Coleta, Preparação e Análise de Dados (CPAD)*
Curso de Ciência da Computação — PUCRS
Grupo: Giovani, Eduardo, Vinicius, João Pedro