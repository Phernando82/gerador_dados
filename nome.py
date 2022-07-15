import random
import string


class nome_email:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


def gera_nome_email():
    lst_nome = [
        'Jessica', 'Marcia', 'Rute',
        'Carolina', 'Bete', 'Josefina',
        'Marcela', 'Ivete', 'Rosa', 'Regina'
    ]
    x = random.randrange(0, 9)
    nome = lst_nome[x]
    aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email = f'{nome.lower()}_{aleatorio.lower()}@gmail.com'
    email_nome = nome_email(nome, email)
    return email_nome


x = gera_nome_email()
print(x.nome)
print(x.email)

# Função que gera nome

# def gera_nome():
#     lst_nome = [
#         'Jessica', 'Marcia', 'Rute',
#         'Carolina', 'Bete', 'Josefina',
#         'Marcela', 'Ivete', 'Rosa', 'Regina'
#     ]
#     x = random.randrange(0, 9)
#     nome = lst_nome[x]
#     return nome
#
#
# def gera_email_nome():
#     nome_email = gera_nome()
#     aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
#     email = f'{nome_email.lower()}_{aleatorio.lower()}@gmail.com'
#     return nome_email, email
