
#Objeto é uma unica coleção de dados(atributos) e comportamentos (metodos)
class ContaBancaria:
    #Atributos são variaveis internas dentro do objeto
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    #Métodos são funções do obejeto que produzem algum comportamento
    def depositar(self, valor):
        self.saldo += valor

    def exibir_detalhes(self):
        print("Número da Conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo: ", round(self.saldo,2))

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

def exibir_menu():
    print("\nMENU:")
    print("1 - Exibir detalhes da conta")
    print("2 - Realizar Depósito")
    print("3 - Realizar Saque")
    print("0 - Sair do Programa")

#aqui estou criando uma instancia do objeto ContaBancaria
#com o nome conta_do usuario
numero_conta = input("Digite o numero da conta")
titular_conta = input("Digite o titular da conta:")
saldo_inicial = float(input("Digite o saldo inicial da conta:").replace(",","."))

conta_do_usuario = ContaBancaria(numero_conta, titular_conta, saldo_inicial)

opcao = None

while opcao != 0:
    exibir_menu()
    opcao = int(input("Digite o numero da opção desejado:"))

    if opcao == 1:
        conta_do_usuario.exibir_detalhes()
    elif opcao == 2:
        valor_deposito = float(input("Digite o valor a ser depositado").replace(",","."))
        conta_do_usuario.depositar(valor_deposito)
    elif opcao == 3:
        valor_saque = float(input("Digite o valor a ser sacado").replace(",","."))
        conta_do_usuario.sacar(valor_saque)