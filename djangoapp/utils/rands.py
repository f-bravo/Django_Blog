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



