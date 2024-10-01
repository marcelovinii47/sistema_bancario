import random
MENU = '''
--------- Sistema bancário ---------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
saldo_bancario = random.uniform(0, 2000)
quantidade_de_saques = 0
MAXIMO_DE_SAQUES = 3

def depositar(saldo_bancario):
    deposito = input("Digite a quantia que deseja depositar: R$ ")
    valor_do_deposito = float(deposito)
    saldo_bancario += valor_do_deposito
    print(f"\nDepósito feito com sucesso! \nSaldo: {saldo_bancario}")

    MENU_DEPOSITAR = """

    [1] Depositar novamente
    [0] Voltar

    
    """

    menu = input(MENU_DEPOSITAR)
    while menu != 0 and menu != 1: 
        if menu == "1":
            print("Depositar novamente")
            depositar(saldo_bancario)
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break

def sacar(saldo_bancario):
    global quantidade_de_saques
    if quantidade_de_saques < MAXIMO_DE_SAQUES:
        saque = input("Digite a quantia que deseja sacar: ")
        valor_saque = float(saque)
        if valor_saque > saldo_bancario:
            print("Saque não efetuado. Valor do saque maior que o saldo bancário.")
        else:
            saldo_bancario -= valor_saque
            print(f"\nSaque feito com sucesso! \nSaldo: {saldo_bancario}")
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
            sacar(saldo_bancario)
            break
        elif menu == "0":
            print("Voltando")
            break
        else:
            print("Seleção de incorreta, tente novamente")
            break


while True:
    opcao = input(MENU)
    print(f"Valor de opcao é: {opcao}")

    if opcao == "1":
        print("Depositar")
        depositar(saldo_bancario)
    elif opcao == "2":
        print("Sacar")
        sacar(saldo_bancario)
    elif opcao == "3":
        print("Extrato")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Seleção incorreta, tente novamente")
        break






