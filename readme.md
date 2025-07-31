# 📋 Sistema de Gestão de Funcionários do Estado - SES

Este sistema tem como objetivo auxiliar os colaboradores na **gestão de funcionários contratados pelo estado em um hospital público**, oferecendo funcionalidades como cadastro, acompanhamento e geração de folha de ponto dos colaboradores.

---

## 💡 Objetivo

Desenvolvido para otimizar a rotina administrativa do hospital, este projeto visa:

- Centralizar os dados dos colaboradores do estado;
- Permitir cadastro, edição e inativação de colaboradores;
- Gerar folhas de ponto mensais em PDF;
- Registrar batidas de ponto manuais;
- Oferecer uma interface simples e funcional para os responsáveis administrativos.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem principal**: Python
- **Framework**: Django
- **Banco de Dados**: SQLite (modo local) e suporte a PostgreSQL
- **Front-end**: HTML + CSS + Bootstrap
- **Servidor**: Debian
- **WSGI Server**: Gunicorn
- **Servidor Web**: Nginx
- **Hospedagem de código**: GitHub
- **Controle de versão**: Git

---

## 🧱 Estrutura do Projeto

```bash
dp_ses/
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── db.sqlite3
├── readme.md
├── manual_instalacao_django_postgresql.md
├── app/                  # Aplicações Django (ex: colaboradores, folha de ponto)
├── templates/            # Templates HTML
├── static/               # Arquivos estáticos (CSS, JS, imagens)
└── ...
```

> A pasta `app/` contém os modelos (models), views e urls específicas para o domínio hospitalar.

---

## 🔧 Instalação e Configuração (Ambiente de Desenvolvimento)

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/dp_ses.git
cd dp_ses
```

### 2. Criar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar banco e aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário

```bash
python manage.py createsuperuser
```

---

## 🚀 Execução Local

```bash
python manage.py runserver
```

Acesse via navegador: [http://localhost:8000](http://localhost:8000)

---

## 📦 Deploy em Servidor Debian (Gunicorn + Nginx)

### Pré-requisitos no servidor:
- Python 3.10+
- Git
- Virtualenv
- Gunicorn
- Nginx

### Passos principais:

1. Clonar o repositório no servidor:

```bash
git clone https://github.com/HRRBC/dp_ses.git
```

2. Criar e ativar ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Aplicar migrações e coletar estáticos:

```bash
python manage.py migrate
python manage.py collectstatic
```

5. Configurar o Gunicorn:

```bash
gunicorn --workers 3 --bind unix:/home/usuario/dp_ses.sock dp_ses.wsgi:application
```

6. Configurar o Nginx com redirecionamento para o socket do Gunicorn.

---

## 🔁 Atualização do Sistema no Servidor

### 1. Acesse o servidor via SSH

```bash
ssh usuario@seu_servidor
cd /caminho/para/dp_ses
```

### 2. Puxe as atualizações do GitHub:

```bash
git pull origin main
```

> Caso você faça push localmente, o GitHub já estará atualizado.

### 3. Reinicie o Gunicorn e o Nginx

```bash
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

---

## 🔧 Manutenção e Expansão

Para novos desenvolvedores:

- Os modelos estão no app `colaboradores`, consulte o arquivo `models.py`.
- Para criar novas funcionalidades:
  - Crie novas views em `views.py`
  - Crie ou edite os templates em `templates/`
  - Adicione novas rotas em `urls.py`
- Sempre crie branches para novos recursos e envie pull requests.
- Documente suas alterações no `CHANGELOG.md` (se aplicável).

---

## 👥 Contribuindo

Sinta-se à vontade para enviar sugestões, relatar problemas ou contribuir com melhorias por meio de pull requests.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.