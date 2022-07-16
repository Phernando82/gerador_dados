import random
import string
import pandas as pd


class nome_email:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


def gera_nome_email():
    df = pd.read_csv('nomes.csv')
    df = df.sample()
    nome = (df['nome'].values[0])
    aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email = f'{nome.lower()}_{aleatorio.lower()}@gmail.com'
    email_nome = nome_email(nome, email)
    return email_nome


# x = gera_nome_email()
# print(x.nome)
# print(x.email)

