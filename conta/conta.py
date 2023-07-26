class Conta:
    def __init__(self, n, cli, sal):
        self.__numero = n
        self.__titular = cli
        self.__saldo = sal

    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def get_info_poupanca(self):
        return f"{self.get_numero()} - ContaPoupanca ({self.__titular})"

    def get_info_corrente(self):
        return f"{self.get_numero()} - ContaCorrente ({self.__titular})"

    def get_info(self):
        if isinstance(self, ContaPoupanca):
            return self.get_info_poupanca()
        elif isinstance(self, ContaCorrente):
            return self.get_info_corrente()

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False


class ContaPoupanca(Conta):
    def __init__(self, n, cli, sal, taxa_juros):
        super().__init__(n, cli, sal)
        self.__taxa_juros = taxa_juros

    def atualizar_juros(self):
        self.__saldo += self.__saldo * self.__taxa_juros


class ContaCorrente(Conta):
    def __init__(self, n, cli, sal, desconto):
        super().__init__(n, cli, sal)
        self.__desconto = desconto

    def sacar(self, valor):
        valor_com_desconto = valor + (valor * self.__desconto)
        return super().sacar(valor_com_desconto)

    def depositar(self, valor):
        valor_com_desconto = valor - (valor * self.__desconto)
        super().depositar(valor_com_desconto)
