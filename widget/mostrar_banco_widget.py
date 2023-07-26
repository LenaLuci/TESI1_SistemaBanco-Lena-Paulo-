import tkinter as tk
from tkinter import ttk

class MostrarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Mostrar Bancos")
        self.geometry("400x300")

        self.banco = banco

        self.banco_list = ttk.Treeview(self, columns=("Número", "Nome", "Juros", "Desconto"), show="headings")
        self.banco_list.heading("Número", text="Número")
        self.banco_list.column('Número', minwidth=80, width=80)
        self.banco_list.heading("Nome", text="Nome")
        self.banco_list.column('Nome', minwidth=120, width=120)
        self.banco_list.heading("Juros", text="Juros")
        self.banco_list.column('Juros', minwidth=60, width=60)
        self.banco_list.heading("Desconto", text="Desconto")
        self.banco_list.column('Desconto', minwidth=80, width=80)
        self.banco_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.populate_treeview()

    def populate_treeview(self):
        self.banco_list.delete(*self.banco_list.get_children())

        numero = self.banco._Banco__numero
        nome = self.banco._Banco__nome
        juros = self.banco._Banco__juros
        desconto = self.banco._Banco__desconto

        self.banco_list.insert("", "end", values=(numero, nome, juros, desconto))
