class Banco:
    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
        self.__contas = []

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def obter_contas(self):
        return self.__contas

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

class Cliente:
    def __init__(self, nome, endereco, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__CPF = cpf

    # Métodos...

class Conta:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    # Métodos...
