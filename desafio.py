menu = """

[d] - Depósito
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 600
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 4

while True:
    
    opcao = input(menu)

    if opcao == "d":
       valor = float(input("Digite o valor do depósito: "))
       
       if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

       else:
          print("A operação falho! O valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        
        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saques = numero_saques >= LIMITES_SAQUES

        if exedeu_saldo:
            print("A operação falhou! Saldo insuficiente.")
        
        elif exedeu_limite:
            print("A operação falhou! O valor do saque solicitado é maior que o limite")
        
        elif exedeu_saques:
            print("A operação falhou! O limete diario de saques foi execido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("A operação falho! O valor informado é inválido.")
        
    elif opcao == "e":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")