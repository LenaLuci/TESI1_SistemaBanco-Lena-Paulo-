class Cliente:
    def __init__(self, n, e, cpf):
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.__vinculado_conta = False
        self.__contas_associadas = []

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__CPF

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def vincular_conta(self, conta):
        self.__contas_associadas.append(conta)

    def desvincular_conta(self, conta):
        self.__contas_associadas.remove(conta)

    def get_contas_associadas(self):
        return self.__contas_associadas
    
