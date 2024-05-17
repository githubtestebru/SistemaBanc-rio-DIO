# Implementar 3 operações: Depósito, saque, extrato.

# Depósito: todos os depósitos devem ser armazenados numa variável e exibidos na operação de extrato
# Saque: o sistema deve permitir realizar 3 saques diários com limite máximo de R$500 por saque, caso o usuário não tenha o saldo em conta o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo, todos os saques devem ser armazenados numa variável e exibidos na operação de extrato
# Extrato: deve listar todos os saques e depósitos efetuados na conta, no fim da listagem deve ser exibido o saldo atual da conta no formato R$xxx.xx 

def getDatetime():
    from datetime import datetime
    datetime = datetime.now()
    mes = str(datetime.month)
    dia = str(datetime.day)
    hora = str(datetime.hour)
    minuto = str(datetime.minute)

    tempo_atual = dia + '/' + mes + ', às ' + hora + ' horas e ' + minuto + ' minutos.'
    
    return tempo_atual

saldo = 0
extrato = ""
contagem_saques = 0

LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3

menu = """
Digite a letra correspondente a opção desejada:

[d] Depósito
[s] Saque
[e] Verificar extrato
[q] Sair

====> """

while True:
    opcao = input(menu)

    if opcao == 'q':
        print('\nOperação encerrada.\n')
        break

    elif opcao == 'd':
        valor = float(input('\nDigite o valor a ser depositado: '))
        
        if valor > 0:
            print('\n => Depósito de R$' + str("%.2f" % valor) + ' efetuado com sucesso!')
            saldo += valor
            extrato += '\nDepósito efetuado: Valor: R$' + str("%.2f" % valor) + '. No dia ' + getDatetime()
        else:
            print('\nOperação inválida! Só é possível depositar valores postivos.')

    elif opcao == 's':
        valor = float(input('\nDigite o valor do saque: '))
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_SAQUE
        excedeu_qtde_saques = contagem_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print('\nSaldo insuficiente. Por favor digite um valor menor que todo seu saldo, ou realize um novo depósito antes de sacar.')

        elif excedeu_limite:
            print('\nNão será possível sacar o dinheiro por extrapolar seu valor limite diário para saques. Por favor digite um valor menor ou igual ao seu limite de R$ 500.00.')

        elif excedeu_qtde_saques:
            print('\nO número diário de saques foi excedido. Por favor, caso deseje sacar mais dinheiro volte outro dia.')
            valor = 0

        elif valor > 0:
            print('\n => Saque de R$' + str("%.2f" % valor) + ' efetuado com sucesso!')
            saldo -= valor
            extrato += '\nSaque efetuado: Valor: R$' + str("%.2f" % valor) + '. No dia ' + getDatetime()
            contagem_saques += 1
        else:
            print('\nOperação inválida! Só é possível sacar valores postivos.')
            
    elif opcao == 'e':
        print()
        print('=' * 30 + ' Extrato ' + '=' * 30)
        print('Não foram feitas movimentações bancárias.' if not extrato else extrato)
        print('\nSaldo atual: R$' + str("%.2f" % saldo))
        print('=' * 69)
    
    else:
        print('\n => Por favor digite uma opção válida, caso deseje encerrar a operação, digite "q".')
