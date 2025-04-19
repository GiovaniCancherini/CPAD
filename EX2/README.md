# EXERCICIO 2

## Configuração do ambiente

### 1. Atualizar o `pip`

```sh
python -m pip install --upgrade pip
```

### 2. Criar e ativar um ambiente virtual

```sh
python -m venv cpad-venv
cpad-venv\Scripts\activate  # Para Windows
source cpad-venv/bin/activate  # Para Linux/Mac
```

Para desativar:

```sh
deactivate
```

### 3. Instalar dependências

```sh
pip install -r requirements.txt
```

## Versões utilizadas

- Python 3.12.6
- PyOpenGL 3.1.9
- PyOpenGL-accelerate 3.1.9

---