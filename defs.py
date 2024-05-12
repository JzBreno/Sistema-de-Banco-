import main
def CriarBarra():
    return print('-'*32 )

def escreve(nomeoperacao, valor):
    extrato = open("extrato.txt", 'a')
    extrato.write(f'{nomeoperacao}: {valor}')
    extrato.close()


def Menu():
    print('+===================+')
    print('|  [1] - Saldo      |')
    print('|  [2] - Depósitar  |')
    print('|  [3] - Extrato    |')
    print('|  [4] - Sacar      |')
    print('|  [5] - Sair       |')
    print('+===================+')
    menu = int(input())
    
    return menu

def Saldo(saldo):
    print(saldo, f'Reais')


def Depositar(saldo):
    nomeoperacao = 'Depositou'
    deposito = int(input("Digite o valor que irá Depositar: "))
    saldo += deposito
    escreve(nomeoperacao, deposito)
    return saldo



def Extrato(extratosaque):
    if len(extratosaque) == 0:
        print("Sem Saques feitos")
    else:
        print("Seu Extrato é: ")
        for i in extratosaque:
            print(i, f'Reais')


def Saque(saldo, limitesaque, extratosaques):
    nomeoperacao = 'Sacou'
    print("Seu limite diario é 500 Reais")
    print(f'Seu limite de saques diarios atualmnete são', limitesaque)
    saque = int(input("Digite o valor que deseja sacar: "))
    if saque <= 500 and limitesaque > 0 and saldo > 0:
        main.limitesaques -= 1
        main.extratosaque.append(saque)
        saldo -= saque
        escreve(nomeoperacao, saque)
        return saldo, main.limitesaques, main.extratosaque
    else:
        if saldo == 0:
            print('Seu saldo está Zerado!')
        if limitesaque == 0:
            print('Seu milite de saques diarios está Zerado!')
        if saque > 500:
            print('Seu limite de saque diario é apenas de 500 Reais')
        return saldo, limitesaque, extratosaques

