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
-> django-admin startproject project .
Teste para ver se o django está ok. Se n tiver feche e abra o VSCode
-> python manage.py runserver
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

# Eu não alterei o defaultBranch para main - deixei como master
# estava dando erro na hora de dar o push

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


#------------------------------------------------------
-> git add . (ou) git add nome_do_arquivo
-> git commit -m 'explicação'
-> git push origin master
# ------------------------------------------------------------
"""


