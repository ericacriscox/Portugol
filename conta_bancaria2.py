class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito de {valor:.2f}")
            print(f"Depósito de {valor:.2f} realizado com sucesso.")
        else:
            print("Valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(f"Saque de {valor:.2f}")
            print(f"Saque de {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque ou valor de saque inválido.")

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo: {:.2f}".format(self.saldo))

    def saldo_medio(self):
        total_transacoes = len(self.transacoes)
        if total_transacoes > 0:
            total_saldo = sum([float(transacao.split()[2]) for transacao in self.transacoes])
            return total_saldo / total_transacoes
        else:
            return 0

    def saldo_negativo(self):
        return self.saldo < 0

    def ultimas_transacoes(self, n=5):
        if n >= len(self.transacoes):
            return self.transacoes
        else:
            return self.transacoes[-n:]

# Função para exibir o menu
def exibir_menu():
    print("\nMENU:")
    print("1. Exibir detalhes da conta")
    print("2. Realizar depósito")
    print("3. Realizar saque")
    print("4. Exibir saldo médio")
    print("5. Verificar saldo negativo")
    print("6. Exibir últimas transações")
    print("0. Sair do programa")

# Solicitando informações do usuário e criando a conta
numero_conta = input("Digite o número da conta: ")
titular_conta = input("Digite o nome do titular da conta: ")
saldo_inicial = float(input("Digite o saldo inicial da conta: "))

conta_do_usuario = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

# Loop principal para exibir o menu e realizar operações
opcao = None
while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor do saque: "))
        conta_do_usuario.sacar(valor_saque)
    elif opcao == 4:
        print("Saldo Médio:", conta_do_usuario.saldo_medio())
    elif opcao == 5:
        if conta_do_usuario.saldo_negativo():
            print("O saldo está negativo.")
        else:
            print("O saldo não está negativo.")
    elif opcao == 6:
        ultimas_transacoes = conta_do_usuario.ultimas_transacoes()
        print("Últimas Transações:")
        for transacao in ultimas_transacoes:
            print(transacao)
    elif opcao == 0:
        print("Encerrando o programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida do menu.")
