# SAEPSaúde

## Como rodar

1. Criar banco PostgreSQL: saepsaude_db

2. Ativar venv

3. Instalar:
pip install -r requirements.txt

4. Criar tabelas:
flask shell
from app import db
db.create_all()

5. Rodar:
python app.py
