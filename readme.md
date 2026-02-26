# 📋 Sistema de Gestão de Funcionários do Estado - SES

Este sistema tem como objetivo auxiliar na **gestão de funcionários contratados pelo estado em um hospital público**, oferecendo funcionalidades como cadastro, acompanhamento e geração de folha de ponto.

---

## 💡 Objetivo

O sistema foi desenvolvido para otimizar a rotina administrativa do hospital, com foco em:

- Centralização de dados dos colaboradores do estado;  
- Cadastro, edição e inativação de colaboradores;  
- Geração de folhas de ponto mensais em PDF;  
- Registro de batidas de ponto manuais;  
- Interface simples e funcional para uso administrativo.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python + Django  
- **Banco de Dados**: PostgreSQL (via Docker)  
- **Frontend**: HTML + CSS + Bootstrap  
- **Containerização**: Docker + Docker Compose  
- **Servidor Web**: Nginx (via Docker)  
- **Sistema Operacional**: Debian  
- **Hospedagem de código**: GitHub  
- **Controle de versão**: Git

---

## 📁 Estrutura do Projeto

```bash
dp_ses/
├── manage.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── nginx/
│   └── default.conf           # Configuração do Nginx
├── dp_ses/
│   └── ...                    # Projeto Django principal
├── dp_ses_management/
│   └── ...                    # App com funcionalidades de gestão
├── static/
│   └── ...                    # Arquivos estáticos (CSS, JS, imagens)
├── templates/
│   └── ...                    # Templates HTML
├── README.md
└── ...
```

---

## 🚀 Como Rodar ou iniciar o Projeto com Docker (Servidor ou Desenvolvimento)

### 1. Pré-requisitos

Certifique-se de que o Docker e Docker Compose estão instalados:

```bash
docker --version
docker compose version
```

### 2. Clonar o repositório

```bash
git clone https://github.com/HRRBC/dp_ses.git
cd dp_ses
```

### 3. Subir os containers

```bash
cd var/dp_ses_app/dp_ses/  #local onde esta salvo
docker compose up -d --build
```

### 4. Acessar o sistema
abra o putty e se conecte ao ip 192.168.140.52

Abra o navegador em: [http://localhost](http://localhost)

> Caso esteja em um servidor, substitua `localhost` pelo IP do servidor.

---

## 🧑‍💻 Comandos Úteis

### Criar superusuário Django (após subir os containers)

```bash
docker compose exec web python manage.py createsuperuser
```

### Aplicar migrações manualmente (caso necessário)

```bash
docker compose exec web python manage.py migrate
```

### Rodar importação de colaboradores via planilha

```bash
docker compose exec web python manage.py importar_colaborador
```

---

## 🔁 Atualização do Sistema no Servidor

1. Acesse o servidor via SSH:

```bash
ssh usuario@IP_DO_SERVIDOR
cd /caminho/para/dp_ses
```

2. Puxe as alterações do repositório:

```bash
git pull origin main
```

3. Reconstrua e reinicie os containers:

```bash
docker compose up -d --build
```

4. Reiniciar todos os containers:

```bash
docker compose restart
```
5. (Opcional) Remover containers órfãos:

```bash
docker compose up -d --remove-orphans
```

---


## 🔧 Manutenção e Expansão

- As funcionalidades estão organizadas no app `dp_ses_management`.  
- Novas funcionalidades devem seguir o padrão MVC do Django.  
- Use branches nomeadas e envie pull requests.  
- Documente mudanças relevantes no `CHANGELOG.md`.

---

## 👥 Contribuindo

Contribuições são bem-vindas! Relate bugs, abra issues ou envie PRs com melhorias.

---

## 📄 Licença

Este projeto está sob a Licença MIT. Veja o arquivo `LICENSE` para mais informações.
