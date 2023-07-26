import tkinter as tk
from tkinter import messagebox

class AtualizarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Atualizar Banco")

        self.banco = banco

        label_numero_banco = tk.Label(self, text="Número do Banco:")
        label_numero_banco.pack()

        self.entry_numero_banco = tk.Entry(self)
        self.entry_numero_banco.pack()

        label_nome_banco = tk.Label(self, text="Nome do Banco:")
        label_nome_banco.pack()

        self.entry_nome_banco = tk.Entry(self)
        self.entry_nome_banco.pack()

        button_atualizar_banco = tk.Button(self, text="Atualizar Banco", command=self.atualizar_banco)
        button_atualizar_banco.pack()

    def atualizar_banco(self):
        novo_numero = self.entry_numero_banco.get()
        novo_nome = self.entry_nome_banco.get()

        self.banco.set_numero(novo_numero)
        self.banco.set_nome(novo_nome)

        messagebox.showinfo("Atualização do Banco", "Informações do banco atualizadas com sucesso!")
