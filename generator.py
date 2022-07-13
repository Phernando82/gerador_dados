from gerador_dados.cabecalho import cria_cabecalho
from gerador_dados.email import gera_email
from gerador_dados.nome import gera_nome
from gerador_dados.telefone import gera_telefone

roda = True

while roda:
    try:
        print(cria_cabecalho())
        option = int(input('Digite suas opções ou 0 para finalizar: '))
        if not 0 <= option <= 7:
            raise ValueError("Opção não existe")
    except ValueError as e:
        print("Valor inválido!", e)
    else:
        if option == 0:
            break
        elif option == 1:
            print(gera_nome())
        elif option == 2:
            print(gera_email())
        elif option == 3:
            print(gera_telefone())
        elif option == 4:
            print('Deus')
        elif option == 5:
            print('Deus')
        elif option == 6:
            print('Deus')
        elif option == 7:
            print('Deus')





    #     if options != 'parar':
    #     print(f'{options} foi digitado')
    #     grava = input('Quer gravar em arquivo txt? Digite S para SIM ou N para não:')
    #     if grava == 's':
    #         print('Será gravado txt')
    #     else:
    #         print('Não será gravado arquivo txt')
    # else:
    #     break
