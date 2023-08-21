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
"""
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists(), 
"""
# Será feita uma coisa para quando o user adicionar um setup ele não possa fazer
# novamente.
# Será usado o método de permissões do django
# Se o método has_add_permission retornar True a pssoa tem permissão de add 
# novos valores. Se retornar False a pessoa não vai ter a permissão.
# Isso é para bloquear na área adminstrativa


# --> 526

# Montando o relacionamento entre MenuLink e SiteSetup

# SiteSetup(1) tem MenuLink(1*) muitos

# Em models.py na class MenuLink add esse trecho:
""" site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE, blank=True, null=True, 
        default=None
    )"""
# class MenuLinkInLine(admin.TabularInline):
#     model = MenuLink
#     extra = 1


# 527 - usando Context Processors para injetar valores em todos os templates

# Ter acesso a um contexto em tods as páginas de tds os apps:
# Context Processors:
# Sem precisar de fazer uma views para injetar esse valor o Django:
# é uma função que recebe a request e retorna um dicionário
# a chave do dicionário vai para o template
# Criando um arquivo em site_setup / constext_processor.py  

""" Criação para teste no constext_processor.py:

from site_setup.models import SiteSetup

def context_processor_example(request):
    return {
        'example': 'Veio do context processor (example)'
    }

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }"""

# Em project/settings.py adicione nos Templates em options add os caminhos:
# 'site_setup.context_processors.context_processor_example',
# 'site_setup.context_processors.site_setup',

# 528

# criando campo ImageFiel para Favicon no Django

# Precisa do Pillow instalado.
# Usando Docker não é simplismente pip install pillow 
# Precisa ir no arquivo requirimets.txt e colocar:
# Pillow>=9.5.0,<9.6
# Agora faça a build novamente
# -> Django_Blog> docker-compose up --build
# com isso ele instala o Pillow e faz as migrações

# Imagem para favicon precisa ser PNG e ter um tamanho pequeno.
# O padrão é 16x16
# em blog/partials/_head.html:
"""coloque com IF - se não envier nenhum favicon não dará erro
{% if site_setup.favicon %}
 <link rel="shortcut icon" href="{{ site_setup.favicon.url}}" type="image/png">
{% endif %}
"""

# Redimencionando a imagem no momento que for enviada:

# 529

# Vamos criar um validador para o campo do favicon para que seja enviado 
# apenas o formato png
# Em djangoapp/site_setup/models.py :
""" import o novo módulo e acrescente o validador: 
from utils.model_validators import validate_png
from utils.images import resize_image

favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True, default='',
        validators=[validate_png],
    )
    # current_favicon_name - antes de salvar
    # self.favicon.name - depois de salvar

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 32)  # redimenciona para 32px
"""

# Em djangoapp crie uma pasta utils/model_validators.py e faça uma função:

"""
from django.core.exceptions import ValidationError

def validate_png(image):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Imagem precisa ser PNG')
"""
# para não deixar o favicon que não seja png ser enviado:
# tem que criar uma exceção importando o ValidationError

# Redimencioanr a imagem:

# precisa fazer um pip install pillow:
# para o ambiente virtual saber que tem o Pillow instalado
# Em djangoapp/utils/images.py :
# será a criada a função resize_image que é para usar o Pillow para 
# redimencionar iamgens.


# 530 - CSS

# Reset CSS mais estruturado 0 remedy.css

# https://github.com/jensimmons/cssremedy/blob/master/css/remedy.css

# Criado o arquivo em blog/cdd/remedy.css 
# faça um link no _head.html - coloque o remedy primeiro
# <link rel="stylesheet" href="{% static 'blog/css/remedy.css' %}">
# <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">

# No CSS será usado um formato para as cores diferente. Veja se é bom, n da erro
# e se da p se daptar numa boa.

# 531 

# Basse do CSS feito.

# blog/partials/_temp.html : arquivo temporário p ajudar no layout
# Foi gerado um arquivo no loripsum.net para por no _temp.html
# No blog/partials/base.html inclua o caminho do arquivo _temp
# {% include 'blog/partials/_temp.html' %}

# 532

# Criando os templates necessários para o Layout:

# Em djangoapp/blog/templates/blog/pages:
# Foi criada mais 2 páginas. A PAge e post além da index.
# Essas 3 páginas jã vão cobrir o blog inteiro.
# O index vai carregar tudo onde tiver vários posts:
# Busca, usuários, categorias, home, tags. Carrega lista de posts
# O page carrega as páginas e o post carrega os posts

# Precisa carregar as páginas para ver. E para isso vamos criar 2 views.
# Em djangoapp/blog/views.py:
"""
def page(request):
    return render(
        request,
        'blog/pages/page.html',
    )
def post(request):
    return render(
        request,
        'blog/pages/post.html',
    )"""
# Feito as views crie as urls:


# 533 

# finalizando a parte de html e css do blog.
# Layout praticamente pronto.

# 535

# Usando o context processor do model site_setup nos templates p/ configurações
# Fazendo a parte de configuração que mostra ou não determinado conteúdo do site
# Colocando um menu link na _header.html:
# Relação de Pai para Filho:
# Site_setup para MenuLink.
# O menuy link tem uma foreingkey para site_setup
# {{ site_setup.menulink_set.all }} 
# Da para colocar mais de um bastando acrescentar na área admin.

# O nome setup está dinâmico. Ele modifica tanto no título da página, na footer
# e o nome que fica no navegador.
# Ao colocar no _head.html:
# <title> {{ site_setup.title }} </title> fina o nome do navegador.


# 536

# criand os models Tag e category + SlugField

# em djangoapp/blog/models.py :

# O autor que criar o post será um usuário do Django.

# Slug é um texto que vai representar a tag na url. É como se fosse um "id"
# Toda vez que for buscar a Tag, vai buscar pela slug. Mesmo ela tento um id.
# Slug é uma url. Não terá acento. Só letras e traços basicamente.
# Como a slug será usada p/ bsucar uma tag ela precisa ser única.
# coloque unique=True.
# Models.py :
"""
from django.db import models
from utils.rands import slugify_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255);
    slug = models.SlugField(
        unique=True, default=None, null=True, blank=True, max_length=255,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs) """ 

# Slug:
"""
# Função que gera letras e números aleatórios
import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
    ))

def slugify_new(text, k=5):
    return slugify(text) + '-' + random_letters(k)

# print(random_letters()) # 1lhnY
# print(slugify('Olá mundo')) # ola-mundo
# Qualquer coisa que tiver no name faça um slugify: transforma numa 'url'
# print(slugify_new('Testando o slugify new')) # testando-o-slugify-new-imcqrnr
"""


# Faça a migração - novamente - docker-compose up

# em blog/admin.py
"""
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }
"""

# 537 


# criando o model e a adimin Page(models.Model e admin.Model.Admim)

# A Page é uma parte do site que usa o cabeçalho, a estrutura toda. Puro html
# E ficará a critério para por o que quiser. É bem mais simples que um post

# identico - criação do PageAdmin: 
"""
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }"""
# identico - criação do model - Page:
"""
class Page(models.Model):
    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True, default="",
        null=False, blank=True, max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisará estar marcado '
            'para a página ser exibida publicamente.'
        ),
    )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title  """


# 538 - 

# Criando o models Post
# blog/models.py :
"""
class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    title = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default="",
        null=True, blank=True, max_length=255,
    )
    excerpt = models.CharField(max_length=150)  # resumo do post
    is_published = models.BooleanField(
        default=False,
        help_text=(
            'Este campo precisará estar marcado '
            'para o post ser exibida publicamente.'
        ),
    )
    # conver = capa do post
    content = models.TextField()
    cover = models.ImageField(upload_to='post/%Y/%m/', blank=True, default='')
    cover_is_post_content = models.BooleanField(
        default=True,
        help_text='Se marcado exibirá a capa dentro do post.',
    )
    # Quando opost for salvo vai adicionar a data do dia.
    created_at = models.DateTimeField(auto_now_add=True)
    # Toda vez que salvar um novo post vai gerar uma nova data
    updated_at = models.DateTimeField(auto_now=True)
    # Category é mãe do post. Uma categoria para muitos posts.
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    # uma tag pode ser utulizaem vários posts ou um post pode ter várias tags
    tags = models.ManyToManyField(Tag, blank=True, default='')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title, 4)
        return super().save(*args, **kwargs)
"""
# Faça a migração:
# -> docker compose run --rm djangoapp migrate.sh

# blog/admin.py
"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published',  'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 50
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by',
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'tags', 'category',"""

# 

