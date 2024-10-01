MENU = '''
--------- Sistema bancário ---------

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

'''
saldo = 0
while True:
    opcao = input(MENU)
    print(f"Valor de opcao é: {opcao}")

    if opcao == "1":
        print("Depositar")
    elif opcao == "2":
        print("Sacar")
    elif opcao == "3":
        print("Extrato")
    elif opcao == "0":
        print("Saindo...")
    else:
        print("Seleção de incorreta, tente novamente")
        break

