import os
import defs
from time import sleep
extratosaque = []
limitesaques = 3
saldo = float()
limitediario = 500
deposito = float()
saque = float()

print("Bem vindo ao banco")



while True:
    
    menu = defs.Menu()
    
    if menu > 0 and 6 > menu:
        match menu:
            case 1:
                defs.Saldo(saldo)
            case 2:
                saldo = defs.Depositar(saldo)
            case 3:
                defs.Extrato(extratosaque)
            case 4:
                saldo, limitesaques, extratosaque = defs.Saque(
                    saldo, limitesaques, extratosaque)
            case 5:
                break

    else:
        print("DIGITE UM NUMERO QUE TENHA FUNCIONALIDADE")
    sleep(3)
    os.system("cls")

with open("extrato.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.readlines()
    for i in texto:
        print(i)