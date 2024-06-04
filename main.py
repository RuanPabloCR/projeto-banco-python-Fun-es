situacao = 1
limite = 500
limite_limite = 0 # ate 3
armazem = []
armazem_Saque = []
saldo = 0
usuarios = []
contas = []
aGENCIA = "0001"
conta2 = []

def deposito(depositovalor, saldoF, extratoD, /):
    
    if depositovalor > 0:
            saldoF = saldoF + depositovalor
            extratoD.append(depositovalor)
            print(f"Valor depositado com sucesso{depositovalor:.2f}:")
    else:
            print("Operação não concluida!")
    return saldoF, extratoD

def Op_saque(*, valor, saldoF, extratoDS):
    if valor > 0 and valor <= 500:
        if saldoF >= valor:
            saldoF = saldoF - valor
            extratoDS.append(valor)
            print("Saldo sacado com sucesso!")
            return saldoF, extratoDS
        else:
            print("Operação de saque fracassada!")
    else:
        ("Operação de saque fracassada!")

def op_extrato(saldoF, /, *, extratoDS, extratoD):
    print("Depositos: ")
    for n in extratoD:
        print(f"R$ {n:.2f}")
    print("\nSaques: ")
    for n in extratoDS:
        print(f"R$ {n:.2f}")
        print(f"\nSaldo atual: R$ {saldoF:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o seu cpf: ")
    usuario = filtrar(cpf, usuarios)

    if usuario:
        print("Ja existe usuario com seu CPF")
        return
    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de naascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla do Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuario criado!!")



def filtrar(cpf, usuarios):
    usuarios_barrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_barrados[0] if usuarios_barrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtrar(cpf, usuarios)
    if usuario:
        print("conta criado!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuario nao encontrado!")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta encontrada.")
        return
    for conta in contas:
        print(f"""\
        Agência:\t{conta['agencia']}
        C/C:\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """)

while situacao == 1:
    print("""
      Operações:
[D] - Depositar
[S] - Sacar
[E] - Extrato
[L] - Sair
[C] - Criar usuario
[A] - Criar conta
[LI] - Listar contas
""")


    escolha = input("Digite a operação a ser realizada: ")

    if escolha.lower() == "d":
        
        print("Operação de deposito:")
        
        deposito_valor = float(input("Qual o valor do depósito:"))

        #função 1

        saldo, armazem = deposito(deposito_valor, saldo, armazem)

    elif escolha.lower() == "s":
        print("Operação de saque")
        if limite_limite < 3:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            #função 2

            saldo, armazem_Saque = Op_saque(valor= valor_saque, saldoF= saldo, extratoDS= armazem_Saque)

            print(armazem_Saque)
            limite_limite = limite_limite + 1
        else:
            print("Operação de saque fracassada!")
    elif escolha.lower() == "e":
        print("Operação de extrato")
        # função 3

        op_extrato(saldo, extratoD=armazem, extratoDS=armazem_Saque)

    elif escolha.lower() == "l":
        print("Operações realizadas. programa encerrado")
        situacao = 0
    elif escolha.lower() == "c":
        criar_usuario(usuarios)
    elif escolha.lower() == "a":
        numero_conta = len(contas) + 1
        conta = criar_conta(aGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif escolha.lower() == 'li':
        listar_contas(contas)

    else:
        print("Comando invalido, tente novamente!")
