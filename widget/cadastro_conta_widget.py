import tkinter as tk
from tkinter import messagebox
from conta.conta import Conta
from cliente.cliente import Cliente

class CadastroContaWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        print("CadastroContaWidget init - parent:", parent)  # depuração
        super().__init__(parent)
        self.title("Nova Conta")
        self.banco = banco

        label_nome_cliente = tk.Label(self, text="Nome do Cliente:")
        label_nome_cliente.pack()

        self.entry_nome_cliente = tk.Entry(self)
        self.entry_nome_cliente.pack()

        label_endereco = tk.Label(self, text="Endereço:")
        label_endereco.pack()

        self.entry_endereco = tk.Entry(self)
        self.entry_endereco.pack()

        label_cpf = tk.Label(self, text="CPF:")
        label_cpf.pack()

        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.pack()

        label_saldo_inicial = tk.Label(self, text="Saldo Inicial:")
        label_saldo_inicial.pack()

        self.entry_saldo_inicial = tk.Entry(self)#, state="disabled")
        self.entry_saldo_inicial.pack()

        button_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_conta)
        button_cadastrar.pack()

    def cadastrar_conta(self):
        nome_cliente = self.entry_nome_cliente.get()
        endereco = self.entry_endereco.get()
        cpf = self.entry_cpf.get()
        saldo_inicial = self.entry_saldo_inicial.get()

        novo_cliente = Cliente(nome_cliente, endereco, cpf)

        nova_conta = Conta(len(self.banco.obter_contas()) + 1, novo_cliente, float(saldo_inicial))

        self.banco.adicionar_conta(nova_conta)

        messagebox.showinfo("Cadastro de Conta", f"Conta cadastrada:\nNome do Cliente: {nome_cliente}\nEndereço: {endereco}\nCPF: {cpf}\nSaldo Inicial: {saldo_inicial}")

        self.destroy()