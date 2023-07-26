from cliente.cliente import Cliente

class Banco:
    def __init__(self, numero, nome):
        self.__num = numero
        self.__nome = nome
        self.__contas = []
        self.__clientes = {}

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def obter_contas(self):
        return self.__contas

    def criar_conta_poupanca(self, numero, titular, saldo_inicial, taxa_juros):
        cliente = self.buscar_cliente_por_cpf(titular)
        if cliente:
            cliente.vincular_conta(numero)
        else:
            cliente = Cliente(titular, "", titular)
            cliente.vincular_conta(numero)
            self.__clientes[titular] = cliente

    def criar_conta_corrente(self, numero, titular, saldo_inicial, desconto):
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
