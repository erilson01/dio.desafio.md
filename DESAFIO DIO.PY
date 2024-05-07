menu = '''

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair 

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

while True: 
    
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('informe o valor do desposito'))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
          print('operaçao falhou! o valor informado é invalido.')

    elif opcao == 's':
        valor = float(input('informe o valor do saque:'))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print('operaçao falhou! você não tem saldo suficente')

        elif excedeu_limite:
            print('operadores falhou! o valor do saque exede o limite.')

        elif excedeu_saques:
            print('operaçao falhou! Número máximo de saque excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print('operaçao falhou! o valor informado é invalido.')

    elif opcao == 'e':
        print('\n==============EXTRATO==============') 
        print('nao foram realizadas movimentaçoes.' if not extrato else extrato)
        print( f'\nSaldo: R$ {saldo:.2F}')
        print('=====================================') 
          
    elif opcao == 'q':
        break

    else:
        print ('operaçao inválida, por favor selecione novamente a operação desejada.')

            



    
