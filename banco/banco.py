from cliente.cliente import Cliente
from conta.conta import ContaPoupanca

class Banco:
    def __init__(self, numero, nome, juros=0, desconto=0):
        self.__numero = numero
        self.__nome = nome
        self.__contas = []
        self.__clientes = {}
        self.__juros = juros
        self.__desconto = desconto

    def get_numero(self):
        return self.__numero

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_juros(self):
        return self.__juros
    
    def set_juros(self, juros):
        self.__juros = juros

    def get_desconto(self):
        return self.__desconto
    
    def set_desconto(self, desconto):
        self.__desconto = desconto

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def criar_cliente(self, nome, cpf, endereco):
        cliente = Cliente(nome, endereco, cpf)
        self.__clientes[cpf] = cliente

    def adicionar_cliente(self, cliente):
        self.__clientes[cliente.get_cpf()] = cliente  # Store cliente object with CPF as the key

    def obter_clientes(self):
        return list(self.__clientes.values())

    def obter_contas(self):
        return self.__contas

    def criar_conta_poupanca(self, numero, titular, saldo_inicial):
        cliente = self.buscar_cliente_por_cpf(titular)
        if cliente:
            cliente.vincular_conta(numero)
        else:
            cliente = Cliente(titular, "", titular)
            cliente.vincular_conta(numero)
            self.__clientes[titular] = cliente

    def criar_conta_corrente(self, numero, titular, saldo_inicial):
        cliente = self.buscar_cliente_por_cpf(titular)
        if cliente:
            cliente.vincular_conta(numero)
        else:
            cliente = Cliente(titular, "", titular)
            cliente.vincular_conta(numero)
            self.__clientes[titular] = cliente

    def buscar_cliente_por_cpf(self, cpf):
        return self.__clientes.get(cpf, None)

    def remover_cliente(self, cpf):
        cliente = self.buscar_cliente_por_cpf(cpf)
        if cliente:
            contas_associadas = cliente.get_contas_associadas()
            if contas_associadas:
                print("Não é possível remover o cliente. O cliente está vinculado a uma ou mais contas.")
            else:
                del self.__clientes[cpf]
                print("Cliente removido com sucesso.")
        else:
            print("Cliente não encontrado.")
            
    def aplicar_juros(self):
        for conta in self.__contas:
            if isinstance(conta, ContaPoupanca):
                conta.depositar(conta.get_saldo() * self.__juros)

    def aplicar_desconto(self, valor):
        return valor - (valor * self.__desconto)
