class Cliente:
    def __init__(self, n, e, cpf):
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.__contas_associadas = []

    def vincular_conta(self, numero_conta):
        self.__contas_associadas.append(numero_conta)

    def desvincular_conta(self, numero_conta):
        self.__contas_associadas.remove(numero_conta)

    def get_contas_associadas(self):
        return self.__contas_associadas
