import random



# função gera telefone

def gera_telefone():
    tel = [random.randint(0, 9) for x in range(8)]
    ddd = random.randint(11, 99)
    tel = f'+55 ({ddd}) 9' + ''.join([str(_) for _ in tel])  # transforma lista em string
    return tel

def gera_telefone_estado(estado):
    tel = [random.randint(0, 9) for x in range(8)]
    dic_estado = {'Amazonas': 92, 'Bahia': 71, 'São Paulo': 11, 'Rondônia': 69,
                  'Mato Grosso': 65, 'Maranhão': 98, 'Mato Grosso do Sul': 67,
                  'Pará': 91, 'Paraíba': 83, 'Tocantins': 63, 'Santa Catarina': 48,
                  'Amapá': 96, 'Paraná': 41, 'Roraima': 95, 'Minas Gerais': 31, 'Espírito Santo:': 27,
                  'Acre': 68, 'Pernambuco': 87, 'Rio de Janeiro': 21, 'Rio Grande do Sul': 51,
                  'Distrito Federal': 61, 'Sergipe': 79, 'Alagoas': 82, 'Rio Grande do Norte': 84,
                  'Ceará': 85, 'Piauí': 86}
    for key in dic_estado.keys():
        if estado in key:
            ddd = dic_estado.get(key)
    tel = f'+55 ({ddd}) 9' + ''.join([str(_) for _ in tel])  # transforma lista em string
    return tel
