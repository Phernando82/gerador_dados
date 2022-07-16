from gerador_dados.cabecalho import cria_cabecalho
from gerador_dados.cpf import cpf_generate
from gerador_dados.endereco import gera_endereco
from gerador_dados.nome import gera_nome_email
from gerador_dados.telefone import gera_telefone

while True:
    try:
        print(cria_cabecalho())
        option = input('Digite suas opções ou 0 para finalizar: ')
        list(option)
        option = [int(i) for i in option]
        dados = {}
        for i in option:
            if not 0 <= i <= 7:
                raise ValueError("Opção não existe")
    except ValueError as e:
        print("Valor inválido!", e)

    else:
        nome_email = gera_nome_email()
        endereco = gera_endereco()
        if 0 in option:
            break
        if 1 in option:
            dados['Nome'] = nome_email.nome
            print(dados['Nome'])
        if 2 in option:
            dados['Email'] = nome_email.email
            print(dados['Email'])
        if 3 in option:
            dados['Telefone'] = gera_telefone()
            print(dados['Telefone'])
        if 4 in option:
            dados['Cidade'] = endereco.city
            print(dados['Cidade'])
        if 5 in option:
            dados['Estado'] = endereco.state
            print(dados['Estado'])
        if 6 in option:
            dados['CPF'] = cpf_generate()
            print(dados['CPF'])
        if 7 in option:
            dados['Nome'] = nome_email.nome
            dados['Email'] = nome_email.email
            dados['Telefone'] = gera_telefone()
            dados['CPF'] = cpf_generate()
            dados['Endereço'] = endereco.address
            dados['Cidade'] = endereco.city
            dados['Estado'] = endereco.state
            dados['CEP'] = endereco.zipcode
            for x, y in dados.items():
                print(str(x) + ": " + str(y))
        print(f'{option} foi digitado')
        grava = input('Quer gravar em arquivo txt? Digite S para SIM ou N para não:').upper()
        if grava == 'S' and 7 in option :
            with open('dados_gerados.txt', 'w') as arquivo:
                arquivo.writelines('Dados gerados:')
                arquivo.writelines('\n')
                arquivo.writelines('\n')
                for x, y in dados.items():
                    arquivo.writelines(str(x) + ": " + str(y)+'\n')
            print('Arquivo txt gravado com sucesso!')

        if grava == 'S' and 7 not in option :
            with open('dados_gerados.txt', 'a') as arquivo:
                arquivo.writelines('\n')
                arquivo.writelines('Dados gerados:')
                arquivo.writelines('\n')
                arquivo.writelines('\n')
                for x, y in dados.items():
                    arquivo.writelines(str(x) + ": " + str(y)+'\n')
            print('Arquivo txt gravado com sucesso!')
        else:
            print('Não será gravado arquivo txt')
