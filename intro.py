# Comandos:

# ------------------------------------------------------

"""
# Iniciando o projeto: 
# Criando o ambiente virtual:
-> python -m venv venv
# Ativando o ambiente virtual no Windows 
-> . venv\Scripts\Activate
# instalando o django
-> pip install django
# Atualizar o pip
-> pip install --upgrade pip
# Startando o project
# Cria uma pasta na raiz - djangoapp
# acesse a pasta djangoapp: C:\Django_Blog> cd djangoapp
-> django-admin startproject project .
# saia da pasta C:\Django_Blog\djangoapp> cd ..

# -->> Raiz alterada para usar o docker <<-- #

# Comando runserver com nova raiz do porjeto:
-> python djangoapp/manage.py runserver
"""

#--------------------------------------------------------


# Configurando o git ignore --> arquivos que não vão para o repositório
"""
crei o .gitignore na raiz do projeto 
busque no google --> django gitignore 
https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
Cole os comandos dentro da pasta .gitignore
"""

"""
# Iniciando o GIT
# -> git init
OBS: usar o mesmo nome e email do GITHUB
# Criando nome de usuário:
-> git config --global user.name 'nome'
# Configurando email:
-> git config --global user.email 'email@email.com'
# Olhando as configurações do GIT:
-> git config --global

# DefaultBranch - master
# Adicioanando: para o git monitorar os arquivos 
-> git add .  - para adicionar tudo

# Dando o primeiro Commit
-> git commit -m 'intro1'

# dando um git log - para ver o que foi feito:
# ou -> git log --oneline
# R: c5ef3d1 (HEAD -> master) Initial

# Crei o repositório no perfil do github
Adicionando o repositório remoto: 
copie a chave https e dê o seguinte comando:
-> git remote add origin https://github.com/f-bravo/Django_agenda.git

# Enviando os commites: 
-> git push origin master -u

# Apague o db.sqlite3 pois será usado o db postgresql


#------------------------------------------------------
-> git add . (ou) git add nome_do_arquivo
-> git commit -m 'explicação'
-> git push origin master
# ------------------------------------------------------------
"""

# dotenv_files:
# .env --> não vai p o github. Aqui coloca as informações reais
# .env-example --> vai p o github

# 517 - configurações:
# dotenv_files(.env, .env-example), dockerignore, settings.py, url.py

# -----------------------------------------------------------------------------

# 518 - Dockerfile 

# continuação das configurações...

""" Avisos:
warning: in the working copy of 'scripts/commands.sh', LF will be replaced by 
CRLF the next time Git touches it
"""

#------------------------------------------------------------------------------

# Dockerfile: 
# Gera a imagem(Django), constrói uma imagem com as configurações

# Para trabalhar com Django precisa de uma base de dados do postgre no Django

""" 
### Tutorial oficial Microsoft p/ instalar o Docker: 
https://docs.microsoft.com/en-us/windows/wsl/install-win10

### Passo 1 (PowerShell Admin): ctrl+v
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

### Passo 2 (PowerShell Admin): ctrl+v
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

### Passo 3
REINICIE O COMPUTADOR

### Passo 4 (Download the Linux kernel update package):
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

### Passo 5 (PowerShell Admin):
wsl --set-default-version 2

### Passo 7 (Instale o docker):
Tutorial: https://docs.docker.com/docker-for-windows/install/
"""

# Reinicie a máquina, abra terminal e teste o comando docker ps ou 
# docker-compose --help. 


# Toda vez que alterar alguma coisa no:
#  Docker-compose, dockerfiile e .env - rebuild a imagem.
# -> docker compose up --build

# Volte para a pasta raiz e entre na pasta do arquivo.
# PS C:\Users\bravo> cd..
# PS C:\Users> cd..
# PS C:\> cd C:\Django_Blog
# PS C:\Django_Blog>

# Finalizada a instalação

# Se n precisar fazer a build, p subir a aplicação django ou apenas subir a app
# -> docker compose up

# Para deixar o docker rodando sem travar o terminal:
# -> docker compose up -d

# para desligar o container:
# docker compose down

# Mas é bom trabalhar podendo ver o que acontece como os prints do Django.
# Basta não usar o comando -d no final e abrir outra aba no terminal.


# -----------------------------------------------------------------------------

# O docker adiciona uma camada de complexidade a mais 
# A vantagem é subir o ambiente de desenvolvimento exatamente igual em todas as 
# máquinas que for usar. Isso é bom para simular o ambiente de produção

# Tudo está configurado para rodar dentro do container.
# Como executar comandos dentro do container?
# Sem nenhum container rodando:

# Exemplo:
# Sempre que subir un container e quiser descer ele use (--rm)
# Para ver a versão do Python:
# -> docker-compose run --rm djangoapp python -V
# Python 3.11.3

# PS C:\Django_Blog> docker-compose run --rm djangoapp pwd
# /djangoapp

# Para executar qualquer comando diretamente:
# -> docker-compose run --rm djangoapp COMANDO

# Criado os scripts collectstatic.sh, makemigrations.sh. migrate.sh, 
# runserver.sh e wait_psql.sh

# Ao alterar os scripts precisa buildar novamente pois as alterações não serão 
# aplicadas. Somente após a nova build.
# -> docker-compose up --build


# ---> 521:


# Criando usper user
# -> docker-compose run --rm djangoapp python manage.py createsuperuser
# nome:
# email:
# senha:

# Criando o app blog:
# terá apenas um app para essa aplicação 
# -> docker-compose run --rm djangoapp python manage.py startapp blog


# crie duas pastas no app:
# static -> crie blog/css/style.css
# templates -> blog/pages/index.html 
# templates/blog -> partials 
# templates/base.html na raiz


# 523 

# Separando os parciais header, pagination e  footer

# Crie os arquivos na pasta partials
# _header.html, _pagination.html e _footer.html
# Coloque um h1 em cada para testar
# no base.html que está na raiz:
""" 
<body>
    {% include 'blog/partials/_header.html' %}
    {% block content %}{% endblock content %}
    {% include 'blog/partials/_pagination.html' %}
    {% include 'blog/partials/_footer.html' %}
</body>
"""

# 524
# Criando o app para as configurações do site: site_setup

# Quando tem um app que não tem relação com outro app geralmente cria separado
# ->  docker-compose run --rm djangoapp python manage.py startapp site_setup

# Criado no djangoapp a pasta site_setup
# A intenção com isso:
# Criar na área administrativa do Django uma parte onde o usuário possa 
# configurar o site. Título, descrição, se vai mostrar header ou não, etc.

# Qualquer cosia que vá usar automaticamente do Django após criar o app precisa
# registrar o nome do app dentro do projetct/settings.py.
# Agora aplique o comando para fazer as migrações.
# Migração:
# -> docker-compose run --rm djangoapp migrate.sh

# Para mostrar o app na área administrativa:
""" site_setup/admin.py 
from django.contrib import admin
from site_setup.models import MenuLink
# Register your models here.

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path',
    list_display_links = 'id', 'text', 'url_or_path',
    search_fields = 'id', 'text', 'url_or_path',
"""

# ---> 525 

# Criando o model SiteSetup e registrando na admin do Django

# from site_setup.models import MenuLink, SiteSetup
# @admin.register(SiteSetup)
# class SiteSetupAdmin(admin.ModelAdmin):
#    list_display = 'title', 'description',

# Será feita uma coisa para quando o user adicionar um setup ele não possa fazer
# novamente.
# Será usado o método de permissões do django
# Se o método has_add_permission retornar True a pssoa tem permissão de add 
# novos valores. Se retornar False a pessoa não vai ter a permissão.


