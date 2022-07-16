
dic_estado = {'Amazonas': 92, 'Bahia': 71, 'São Paulo': 11, 'Rondônia': 69,
                  'Mato Grosso': 65, 'Maranhão': 98, 'Mato Grosso do Sul': 67,
                  'Pará': 91, 'Paraíba': 83, 'Tocantins': 63, 'Santa Catarina': 48,
                  'Amapá': 96, 'Paraná': 41, 'Roraima': 95, 'Minas Gerais': 31, 'Espírito Santo:': 27,
                  'Acre': 68, 'Pernambuco': 87, 'Rio de Janeiro': 21, 'Rio Grande do Sul': 51,
                  'Distrito Federal': 61, 'Sergipe': 79, 'Alagoas': 82, 'Rio Grande do Norte': 84,
                  'Ceará': 85, 'Piauí': 86}

for key in dic_estado.keys():
  if 'Pará' in key:
    tof = dic_estado.get(key)
    break
print(tof)