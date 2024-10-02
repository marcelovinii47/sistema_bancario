import random
MENU = '''
--------- Sistema bancário ---------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
saldo_bancario = random.uniform(0, 2000)
print(saldo_bancario)
quantidade_de_saques = 0
MAXIMO_DE_SAQUES = 3
valor_sacado = 0
valor_depositado = 0
def depositar():
    global valor_depositado
    global saldo_bancario
    deposito = input("Digite a quantia que deseja depositar: R$ ")
    valor_do_deposito = float(deposito)
    print(f"Valor do depósito: {valor_do_deposito}")
    if valor_do_deposito < 0:
        print("Valor digitado não é possível ser depositado. \nTente novamente...")
        depositar(saldo_bancario)

    else:
        saldo_bancario += valor_do_deposito
        print(f"Valor do saldo bancário: {saldo_bancario}")
        valor_depositado += valor_do_deposito
        print(f"Valor do valor total depositado: {valor_depositado}")
        saldo_formatado = f"R$ {saldo_bancario:,.2f}"
        print(f"\nDepósito feito com sucesso! \nSaldo: {saldo_formatado}")

    MENU_DEPOSITAR = """

    [1] Depositar novamente
    [0] Voltar

    
    """

    menu = input(MENU_DEPOSITAR)
    while menu != 0 and menu != 1: 
        if menu == "1":
            print("Depositar novamente")
            depositar()
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break
    
    return saldo_bancario

def sacar():
    global quantidade_de_saques
    global valor_sacado
    global saldo_bancario
    if quantidade_de_saques < MAXIMO_DE_SAQUES:
        saque = input("Digite a quantia que deseja sacar: ")
        valor_saque = float(saque)
        print(f"Valor do saque: {valor_saque}")
        if valor_saque > saldo_bancario:
            print("Saque não efetuado. Valor do saque maior que o saldo bancário.")
        else:
            saldo_bancario -= valor_saque
            print(f"Valor do saldo: {saldo_bancario}")
            valor_sacado += valor_saque
            print(f"Valor total sacado: {valor_sacado}")
            saldo_formatado = f"R$ {saldo_bancario:,.2f}"
            print(f"\nSaque feito com sucesso! \nSaldo: {saldo_formatado}")
            quantidade_de_saques += 1    
            print(f"Saques restantes no dia: {MAXIMO_DE_SAQUES - quantidade_de_saques}")
    else:
        print("Não foi possível efetuar o saque devido a falta de saques suficientes diários")    

    MENU_SACAR = """

    [1] Sacar novamente
    [0] Voltar

    """ 

    menu = input(MENU_SACAR)

    while menu != 0 and menu != 1: 
        if menu == "1":
            print("Sacar novamente")
            sacar()
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break

    return saldo_bancario

def extrato(valor_sacado, valor_depositado):
    global saldo_bancario
    print(f"Valor total depositado: {valor_depositado:,.2f}")
    print(f"\nValor total sacado: {valor_sacado:,.2f}")
    print(f"Saldo bancário atual: {saldo_bancario:,.2f}")


while True:
    opcao = input(MENU)

    if opcao == "1":
        print("Depositar")
        depositar()
    elif opcao == "2":
        print("Sacar")
        sacar()
    elif opcao == "3":
        print("Extrato")
        extrato(valor_sacado, valor_depositado)
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Seleção incorreta, tente novamente")






