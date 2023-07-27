import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco

class CadastroBancoWidget(tk.Toplevel):
    def __init__(self, parent, lista_bancos):
        super().__init__(parent)
        self.title("Cadastrar Banco")
        self.geometry("400x200")

        self.lista_bancos = lista_bancos

        label_nome = tk.Label(self, text="Nome do Banco:")
        label_nome.pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()

        label_juros = tk.Label(self, text="Juros (%):")
        label_juros.pack()
        self.entry_juros = tk.Entry(self)
        self.entry_juros.pack()

        label_desconto = tk.Label(self, text="Desconto (%):")
        label_desconto.pack()
        self.entry_desconto = tk.Entry(self)
        self.entry_desconto.pack()

        button_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_banco)
        button_cadastrar.pack()

    def cadastrar_banco(self):
        nome = self.entry_nome.get()
        juros = float(self.entry_juros.get()) / 100.0
        desconto = float(self.entry_desconto.get()) / 100.0

        if not nome:
            messagebox.showerror("Erro", "O nome do banco não pode estar vazio.")
            return

        banco = Banco(numero=len(self.lista_bancos) + 1, nome=nome, juros=juros, desconto=desconto)
        self.lista_bancos.append(banco)

        messagebox.showinfo("Cadastro Efetuado", "Banco cadastrado com sucesso!")
        self.destroy()