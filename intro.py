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

