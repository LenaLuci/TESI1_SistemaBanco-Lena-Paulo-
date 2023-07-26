import tkinter as tk
from tkinter import messagebox

class CriarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Criar Banco")

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

        label_desconto_banco = tk.Label(self, text="Número:")
        label_numero_banco.pack()
        self.entry_numero_banco = tk.Entry(self)
        self.entry_numero_banco.pack()

        button_atualizar_banco = tk.Button(self, text="Atualizar Banco", command=self.atualizar_banco)
        button_atualizar_banco.pack()

    def atualizar_banco(self):
        novo_numero = self.entry_numero_banco.get()
        novo_nome = self.entry_nome_banco.get()

        self.banco.set_numero(novo_numero)
        self.banco.set_nome(novo_nome)

        messagebox.showinfo("Atualização do Banco", "Informações do banco atualizadas com sucesso!")