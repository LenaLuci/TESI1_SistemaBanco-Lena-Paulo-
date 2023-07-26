import tkinter as tk
from tkinter import messagebox
from ..classbanco.banco import ContaPoupanca, ContaCorrente

class CriarContaWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Criar Conta")

        self.banco = banco

        label_titular = tk.Label(self, text="Titular:")
        label_titular.pack()
        self.entry_titular = tk.Entry(self)
        self.entry_titular.pack()

        label_saldo = tk.Label(self, text="Saldo Inicial:")
        label_saldo.pack()
        self.entry_saldo = tk.Entry(self)
        self.entry_saldo.pack()

        self.tipo_conta_var = tk.StringVar()
        self.tipo_conta_var.set("ContaPoupanca")

        label_tipo_conta = tk.Label(self, text="Tipo de Conta:")
        label_tipo_conta.pack()

        self.tipo_conta_radio_poupanca = tk.Radiobutton(self, text="Conta Poupança", variable=self.tipo_conta_var, value="ContaPoupanca")
        self.tipo_conta_radio_poupanca.pack()

        self.tipo_conta_radio_corrente = tk.Radiobutton(self, text="Conta Corrente", variable=self.tipo_conta_var, value="ContaCorrente")
        self.tipo_conta_radio_corrente.pack()

        button_criar_conta = tk.Button(self, text="Criar Conta", command=self.criar_conta)
        button_criar_conta.pack()

    def criar_conta(self):
        titular = self.entry_titular.get()
        saldo_inicial = float(self.entry_saldo.get())
        tipo_conta = self.tipo_conta_var.get()

        if tipo_conta == "ContaPoupanca":
            conta = ContaPoupanca(None, titular, saldo_inicial, 0.01)
        else:
            conta = ContaCorrente(None, titular, saldo_inicial, 0.05)

        self.banco.adicionar_conta(conta)
        messagebox.showinfo("Conta Criada", f"Conta criada com sucesso!\nNúmero da conta: {conta.get_numero()}")

        self.destroy()
