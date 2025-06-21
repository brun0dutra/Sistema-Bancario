#Var e Const
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUE = 3

#Menu do Terminal
menu = """
########## MENU ##########
#                        #
# [d] - Depositar        #
# [s] - Sacar            #
# [e] - Extrato          #
# [q] - Sair             #
#                        #
##########################
"""

#Enquanto verdadeiro
while True:

    #Chama o menu e pega a opção desejada
    op = input(menu)

    #Depositar
    if op == "d":

        #Pede o valor do deposito
        valor = float(input(" Qual valor deseja depositar: R$ "))

        #Verifica se é > 0
        if valor > 0:

            #Adiciona o valor na conta
            saldo += valor

            #Adiciona a operação no extrato
            extrato += f"Deposito: R$ {valor:.2f}\n"

            #Mensagem de operação realizada com sucesso
            print("Deposito realizado com SUCESSO !")

        #Se o valor de deposito for <= 0 Mostra mensagem de erro
        else:
            print("Valor invalido, tente novamente !")

    #Sacar
    elif op == "s":

        #Mostra o saldo na conta
        print(f"Valor na conta é de: R$ {saldo:.2f}")
        #Pega o valor de saque desejado
        valor = float(input("Qual valor deseja sacar: R$ "))

        #Verifica se o valor de saque é maior que o saldo
        saldo_insuficiente = valor > saldo
        #Verifica se o valor de saque é maior que o limite
        ultrapassou_limite = valor > limite
        #Verifica se já atingiu o limite de saques diarios
        ultrapassou_saques = numeros_saques >= LIMITE_SAQUE

        #Se o valor do saque for maior que o saldo mostra mensagem
        if saldo_insuficiente:
            print("Saldo Insuficiente")

        #Se ultrappasou o limite mostra a mensagem
        elif ultrapassou_limite:
            print("Valor acima do Limite")

        #Se atingiu o numero de saques diarios mostra a mensagem
        elif ultrapassou_saques:
            print("Você atingiu o limite de saques diarios")

        #Se estiver tudo ok, verifica se o valor é maior que 0 
        elif valor > 0:

            #Acrescenta 1 em vezes que sacou
            numeros_saques += 1
            #Diminui o valor da conta
            saldo -= valor
            #Registra no extrato
            extrato += f"Retirada: R$ {valor:.2f}\n"
            #Mostra mensagem de orientação para retirada do dinheiro
            print("Contando Notas...")
            print("Retire o dinheiro na boca do caixa !")

        #Se nao atender nenhuma das anteriores mostra mensagem
        else:
            print("Informe um valor valido")

    #Extrato
    elif op == "e":
        print("########## EXTRATO ##########")
        print("Não foram realizadas movimentações." if not extrato else extrato) #Se nao tiver nada em extrato, mostrar mensagem, caso tenha mostrar extrato
        print("#############################")
        print(f"Saldo na conta: R$ {saldo:.2f}")
        print("#############################")

    #Sair
    elif op == "q":
        break

    #Caso nao seja nenhuma das opções acima
    else:
        print("Por Favor, Insira uma opção valida !")