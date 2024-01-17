# Criar um novo ambiente virtual
python -m venv ./venv

# Criar o ambiente virtual (Mac)
python3 -m venv ./venv

# Ativar o ambiente virtual (Mac/Linux)
source nome_do_ambiente/bin/activate

# Ativar o ambiente virtual (Windows)
.\nome_do_ambiente\Scripts\activate

# Desativar o ambiente virtual
deactivate

# Comando para instalar dependências
pip install requests

# Listar no terminal todas as dependências e suas versões
pip freeze

# Criar o arquivo que documenta todas as dependências e suas versões
pip freeze > requirements.txt
