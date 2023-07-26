import tkinter as tk
from tkinter import ttk

class MostrarContasWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Mostrar Contas")
        self.geometry("400x300")

        self.banco = banco

        self.account_list = ttk.Treeview(self, columns=("Número", "Titular", "Saldo"), show="headings")
        self.account_list.heading("Número", text="Número")
        self.account_list.column('Número', minwidth=120, width=120)
        self.account_list.heading("Titular", text="Titular")
        self.account_list.column('Titular', minwidth=120, width=120)
        self.account_list.heading("Saldo", text="Saldo")
        self.account_list.column('Saldo', minwidth=120, width=120)
        self.account_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.populate_accounts()

    def populate_accounts(self):
        self.account_list.delete(*self.account_list.get_children())

        contas = self.banco.obter_contas()
        for conta in contas:
            cliente_nome = conta._Conta__titular._Cliente__nome
            saldo = conta._Conta__saldo
            self.account_list.insert("", "end", values=(conta._Conta__numero, cliente_nome, saldo))
