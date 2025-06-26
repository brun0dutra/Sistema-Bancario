def menu():
    menu = """
########## MENU ##########
#                        #
# [d] - Depositar        #
# [s] - Sacar            #
# [e] - Extrato          #
# [n] - Nova Conta       #
# [l] - Listar Contas    #
# [u] - Novo Ususario    #
# [q] - Sair             #
#                        #
##########################
"""
    return input(menu)

def depositar(saldo, valor, extrato, /):
    #Verifica se é > 0
    if valor > 0:

        #Adiciona o valor na conta
        saldo += valor

        #Adiciona a operação no extrato
        extrato += f"Deposito: R$ {valor:.2f}\n"

        #Mensagem de operação realizada com sucesso
        print("Deposito realizado com SUCESSO !")

        return saldo, extrato
    #Se o valor de deposito for <= 0 Mostra mensagem de erro
    else:
        print("Valor invalido, tente novamente !")

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saque):

    #Verifica se o valor de saque é maior que o saldo
    saldo_insuficiente = valor > saldo
    #Verifica se o valor de saque é maior que o limite
    ultrapassou_limite = valor > limite
    #Verifica se já atingiu o limite de saques diarios
    ultrapassou_saques = numeros_saques >= limite_saque

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
        return saldo, extrato, numeros_saques

    #Se nao atender nenhuma das anteriores mostra mensagem
    else:
        print("Informe um valor valido")

def mostrar_extrato(saldo, /, *, extrato):
    print("########## EXTRATO ##########")
    print("Não foram realizadas movimentações." if not extrato else extrato) #Se nao tiver nada em extrato, mostrar mensagem, caso tenha mostrar extrato
    print("#############################")
    print(f"Saldo na conta: R$ {saldo:.2f}")
    print("#############################")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

def criar_usuario(usuarios):
    cpf = str(input("Informe seu CPF: "))
    user = filtrar_usuario(cpf, usuarios)
    if user:
        print("CPF informado já esta em uso !")
    else:
        nome = str(input("Nome Completo: "))
        data_nascimento = str(input("Data de Nacimento nesse padrão (DD-MM-AAAA): "))
        endereco = str(input("Endereço (Logradouro, Numero - Bairro - Cidade/Sigla Estado): "))

        usuarios.append({"nome":nome, "data de nascimento":data_nascimento,"cpf":cpf ,"endereco":endereco})
        print("Usuario Criado Com Sucesso !!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o CPF do usuario: "))
    user = filtrar_usuario(cpf, usuarios)

    if user:
        print("Conta criada com SUCESSO !!")
        return {"agencia":agencia, "numero_conta":numero_conta + 1, "usuario":user}
    
    else:
        print("Usuario não encontrado !")

def listar_conta(contas):
    for conta in contas:
        print(f"""
========================================================
Agencia: {conta['agencia']}
Numero Da Conta: {conta['numero_conta']}
Usuario: {conta['usuario']['nome']}""")

def main():
    #Var e Const
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    LIMITE_SAQUE = 3
    usuarios = [{"nome":"Bruno Dutra", "Data de nascimento":"09-10-1997","cpf":"1234567890" ,"endereco":"Washington Bandeira, 2406 - Mascarenhas De Morais - Bagé/RS" }]
    contas = []
    AGENCIA = '0001'
    num_contas = 0

    #Enquanto verdadeiro
    while True:

        #Chama o menu e pega a opção desejada
        op = menu()

        #Depositar
        if op == "d":
            valor = float(input("Qual valor deseja depositar : R$ "))
            saldo , extrato = depositar(saldo,valor,extrato)

        #Sacar
        elif op == "s":
            #Mostra o saldo na conta
            print(f"Valor na conta é de: R$ {saldo:.2f}")
            #Pega o valor de saque desejado
            valor = float(input("Qual valor deseja sacar: R$ "))
            #Chama função saque
            saldo, extrato, numeros_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numeros_saques=numeros_saques, limite_saque=LIMITE_SAQUE)

        #Extrato
        elif op == "e":
            mostrar_extrato(saldo, extrato=extrato)

        #Criar Conta
        elif op == "n":
            conta = criar_conta(AGENCIA, num_contas, usuarios)

            if conta:
                contas.append(conta)
                num_contas += 1

        #Listar Contas
        elif op == "l":
            listar_conta(contas)

        #Criar Usuario
        elif op == "u":
            criar_usuario(usuarios)

        #Sair
        elif op == "q":
            break

        #Caso nao seja nenhuma das opções acima
        else:
            print("Por Favor, Insira uma opção valida !")

main()