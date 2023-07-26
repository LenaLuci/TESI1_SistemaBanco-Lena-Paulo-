import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco
from conta.conta import ContaPoupanca, ContaCorrente


class CriarContaWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.wm_iconbitmap('poggiebank.ico')
        self.title("Criar Conta")
        self.geometry('300x200')

        self.banco = banco

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        label_titular = tk.Label(frame_principal, text="Titular:", bg='#3366cc')
        label_titular.pack(ipady=2)
        self.entry_titular = tk.Entry(frame_principal)
        self.entry_titular.pack(ipady=2)

        label_saldo = tk.Label(frame_principal, text="Saldo Inicial:", bg='#3366cc')
        label_saldo.pack(ipady=2)
        self.entry_saldo = tk.Entry(frame_principal)
        self.entry_saldo.pack(ipady=2)

        self.tipo_conta_var = tk.StringVar()
        self.tipo_conta_var.set("ContaPoupanca")

        label_tipo_conta = tk.Label(frame_principal, text="Tipo de Conta:", bg='#3366cc')
        label_tipo_conta.pack()

        self.tipo_conta_radio_poupanca = tk.Radiobutton(frame_principal, text="Conta Poupança",
                                                    variable=self.tipo_conta_var, value="ContaPoupanca", bg='#3366cc')
        self.tipo_conta_radio_poupanca.pack()

        self.tipo_conta_radio_corrente = tk.Radiobutton(frame_principal, text="Conta Corrente",
                                                    variable=self.tipo_conta_var, value="ContaCorrente", bg='#3366cc')
        self.tipo_conta_radio_corrente.pack()

        button_criar_conta = tk.Button(frame_principal, text="Criar Conta", command=self.criar_conta)
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
