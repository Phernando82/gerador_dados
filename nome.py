import random
import string


# Função que gera nome

def gera_nome():
    lst_nome = [
        'Jessica', 'Marcia', 'Rute',
        'Carolina', 'Bete', 'Josefina',
        'Marcela', 'Ivete', 'Rosa', 'Regina'
    ]
    x = random.randrange(0, 9)
    nome = lst_nome[x]
    return nome





