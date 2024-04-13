menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "q":
        break

    elif opcao == "d":
        valor = float(input("Digite o valor a ser depositado\n"))

        if valor > 0:
            saldo += valor
            extrato = f"Depósito: R$ {valor: .2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado\n"))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")

        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.\n")

        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(numero_saques)

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "e":
        print("\n================ EXTRATO ================")

        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")


    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
