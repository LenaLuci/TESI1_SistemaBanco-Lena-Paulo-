import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco

class CriarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Criar Banco")
        self.geometry('200x300')

        self.wm_iconbitmap('poggiebank.ico')

        self.banco = banco

        # Criacao de Banco, Numero, nome (taxa de saldo, deposito)
        label_numero_banco = tk.Label(self, text="Número:")
        label_numero_banco.pack()
        self.entry_numero_banco = tk.Entry(self)
        self.entry_numero_banco.pack()
        # defini min 4, max 4, numero

        label_nome_banco = tk.Label(self, text="Nome:")
        label_nome_banco.pack()
        self.entry_nome_banco = tk.Entry(self)
        self.entry_nome_banco.pack()

        label_juros_banco = tk.Label(self, text="Taxa de Juros:")
        label_juros_banco.pack()
        self.entry_juros_banco = tk.Entry(self)
        self.entry_juros_banco.pack()

        label_desconto_banco = tk.Label(self, text="Desconto:")
        label_desconto_banco.pack()
        self.entry_desconto_banco = tk.Entry(self)
        self.entry_desconto_banco.pack()

        button_criar_banco = tk.Button(self, text="Criar Banco", command=self.criar_banco)
        button_criar_banco.pack()

    def criar_banco(self):
        numero = self.entry_numero_banco.get()
        nome = self.entry_nome_banco.get()
        juros = float(self.entry_juros_banco.get())
        desconto = float(self.entry_desconto_banco.get())

        banco = Banco(numero, nome, juros, desconto)

        messagebox.showinfo("Cadastro de Banco", "Banco criado com sucesso!")
        self.destroy()
