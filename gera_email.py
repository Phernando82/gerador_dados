import random

import string
from gerador_dados.nome import gera_nome


# função gera email

def gera_email():
    nome_email = gera_nome()
    aleatorio = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    email = f'{nome_email.lower()}_{aleatorio.lower()}@gmail.com'
    return email




