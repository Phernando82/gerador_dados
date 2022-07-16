# função gera telefone
import random


def gera_telefone():
    tel = [random.randint(0, 9) for x in range(8)]
    tel = '+55(11)9' + ''.join([str(_) for _ in tel])  # transforma lista em string
    return tel



