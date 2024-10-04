import random
MENU = f'''
--------- Sistema bancário ---------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

--> '''
saldo_bancario = random.uniform(0, 2000)
quantidade_de_saques = 0
MAXIMO_DE_SAQUES = 3
valor_sacado = 0
valor_depositado = 0
extrato_str = ""
def depositar(saldo_bancario, valor_depositado, extrato_str):
    deposito = input("Digite a quantia que deseja depositar: R$ ")
    valor_do_deposito = float(deposito)
    if valor_do_deposito <= 0:
        print("Valor digitado não é possível ser depositado. \nTente novamente...")
        saldo_bancario, valor_depositado = depositar(saldo_bancario, valor_depositado, extrato_str)

    else:
        saldo_bancario += valor_do_deposito
        valor_depositado += valor_do_deposito
        saldo_formatado = f"R$ {saldo_bancario:,.2f}"
        print(f"\nDepósito feito com sucesso! \nSaldo: {saldo_formatado}")
        extrato_str += f"\nDepósito feito de R$ {valor_do_deposito:,.2f}"

    MENU_DEPOSITAR = '''

    [1] Depositar novamente
    [0] Voltar

    --> '''
    

    menu = input(MENU_DEPOSITAR)
    while menu != 0 and menu != 1: 
        if menu == "1":
            print("Depositar novamente")
            saldo_bancario, valor_depositado, extrato_str = depositar(saldo_bancario, valor_depositado, extrato_str)
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break
    
    return saldo_bancario, valor_depositado, extrato_str

def sacar(saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str):
    if quantidade_de_saques < MAXIMO_DE_SAQUES:
        saque = input("Digite a quantia que deseja sacar: ")
        valor_saque = float(saque)
        if valor_saque > saldo_bancario:
            print("Saque não efetuado. Valor do saque maior que o saldo bancário.")
        else:
            saldo_bancario -= valor_saque
            valor_sacado += valor_saque
            saldo_formatado = f"R$ {saldo_bancario:,.2f}"
            print(f"\nSaque feito com sucesso! \nSaldo: {saldo_formatado}")
            extrato_str += f"\nSaque feito de {valor_saque:,.2f}"
            quantidade_de_saques += 1    
            print(f"Saques restantes no dia: {MAXIMO_DE_SAQUES - quantidade_de_saques}")
    else:
        print("Não foi possível efetuar o saque devido a falta de saques suficientes diários")    

    MENU_SACAR = '''

    [1] Sacar novamente
    [0] Voltar

    -->'''

    menu = input(MENU_SACAR)

    while menu != 0 and menu != 1: 
        if menu == "1":
            print("Sacar novamente")
            saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str = sacar(saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str)
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break

    return saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str

def extrato(saldo_bancario, valor_sacado, valor_depositado, extrato_str):
    print("------------------------ Extrato Bancário ------------------------")
    print(extrato_str)

    print(f"Valor total depositado: {valor_depositado:,.2f}")
    print(f"Valor total sacado: {valor_sacado:,.2f}")
    print(f"Saldo bancário atual: {saldo_bancario:,.2f}")

    print("------------------------ Extrato Bancário ------------------------")

    return saldo_bancario, valor_sacado, valor_depositado, extrato_str


while True:
    opcao = input(MENU)

    if opcao == "1":
        print("Depositar")
        saldo_bancario, valor_depositado, extrato_str = depositar(saldo_bancario, valor_depositado, extrato_str)
    elif opcao == "2":
        print("Sacar")
        saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str = sacar(saldo_bancario, valor_sacado, quantidade_de_saques, extrato_str)
    elif opcao == "3":
        print("Extrato")
        saldo_bancario, valor_sacado, valor_depositado, extrato_str = extrato(saldo_bancario, valor_sacado, valor_depositado, extrato_str)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Seleção incorreta, tente novamente")






