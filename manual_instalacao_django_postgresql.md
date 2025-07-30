
# 📘 Manual de Instalação e Execução do Projeto Django com PostgreSQL

> Este guia orienta a instalação e execução do projeto Django em um novo ambiente (servidor ou outra instituição).

---

## 🔧 Requisitos

Certifique-se de que os seguintes pacotes estejam instalados:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git postgresql libpq-dev
```

---

## 📁 1. Clonar o repositório do projeto

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```

---

## 🐍 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ 4. Criar o banco de dados PostgreSQL

### Acessar o PostgreSQL:

```bash
sudo -u postgres psql
```

### Criar o banco e o usuário:

```sql
CREATE DATABASE nome_do_banco;
CREATE USER nome_do_usuario WITH PASSWORD 'senha_segura';
ALTER ROLE nome_do_usuario SET client_encoding TO 'UTF8';
ALTER ROLE nome_do_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE nome_do_usuario SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO nome_do_usuario;
\q
```

---

## ⚙️ 5. Configurar o banco de dados no Django

Edite o arquivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'nome_do_usuario',
        'PASSWORD': 'senha_segura',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

---

## 📐 6. Aplicar as migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 7. Criar superusuário

```bash
python manage.py createsuperuser
```

---

## ✅ 8. Testar execução do projeto

```bash
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Testar conexão com o banco (opcional)

```bash
psql -h localhost -U nome_do_usuario -d nome_do_banco
```

---

## 🧼 Extras

- Resetar banco (remover todos os dados):
  ```bash
  python manage.py flush
  ```

- Atualizar lista de dependências:
  ```bash
  pip freeze > requirements.txt
  ```

---

## 🚀 (Opcional) Deploy com Gunicorn + Nginx

Se quiser configurar para produção com Gunicorn, Nginx e systemd, veja o arquivo `DEPLOY.md` (ou peça ajuda 😄).

---
