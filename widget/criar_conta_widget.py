import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conta.conta import Conta

class CriarContaWidget(tk.Toplevel):
    def __init__(self, parent, lista_bancos, lista_clientes):
        super().__init__(parent)
        self.title("Criar Conta")
        self.geometry("400x300")

        self.lista_bancos = lista_bancos
        self.lista_clientes = lista_clientes

        self.titular_label = tk.Label(self, text="Titular:")
        self.titular_label.pack()
        self.titular_var = tk.StringVar()
        self.titular_combobox = ttk.Combobox(self, textvariable=self.titular_var, values=[cliente.get_nome() for cliente in self.lista_clientes])
        self.titular_combobox.pack()

        label_banco = tk.Label(self, text="Banco:")
        label_banco.pack()
        self.banco_var = tk.StringVar()
        self.banco_combobox = ttk.Combobox(self, textvariable=self.banco_var)
        self.banco_combobox['values'] = [banco.get_nome() for banco in self.lista_bancos]
        self.banco_combobox.pack()

        label_tipo_conta = tk.Label(self, text="Tipo de Conta:")
        label_tipo_conta.pack()
        self.tipo_conta_var = tk.StringVar()
        self.tipo_conta_combobox = ttk.Combobox(self, textvariable=self.tipo_conta_var, values=["Conta Poupança", "Conta Corrente"])
        self.tipo_conta_combobox.pack()

        label_saldo = tk.Label(self, text="Saldo:")
        label_saldo.pack()
        self.saldo_entry = tk.Entry(self)
        self.saldo_entry.pack()

        button_criar_conta = tk.Button(self, text="Criar Conta", command=self.criar_conta)
        button_criar_conta.pack()

    def criar_conta(self):
        nome_banco = self.banco_var.get()
        titular = self.titular_var.get()
        tipo_conta = self.tipo_conta_var.get()
        saldo = float(self.saldo_entry.get())

        if not nome_banco:
            messagebox.showerror("Erro", "Selecione um banco para criar a conta.")
            return

        if not titular:
            messagebox.showerror("Erro", "Selecione um titular para criar a conta.")
            return

        if tipo_conta not in ["Conta Poupança", "Conta Corrente"]:
            messagebox.showerror("Erro", "Selecione um tipo de conta válido.")
            return

        if saldo < 0:
            messagebox.showerror("Erro", "O saldo não pode ser negativo.")
            return

        banco = next((banco for banco in self.lista_bancos if banco.get_nome() == nome_banco), None)

        if banco:
            cliente = next((cliente for cliente in banco.clientes if cliente.get_nome() == titular), None)

            if cliente:
                if tipo_conta == "Conta Poupança":
                    conta = Conta(banco, cliente, "Poupança", saldo)
                    banco.adicionar_conta(conta)
                    messagebox.showinfo("Conta Criada", f"Conta Poupança criada para {titular} no banco {nome_banco} com saldo de {saldo:.2f}.")
                    self.destroy()
                else:
                    conta = Conta(banco, cliente, "Corrente", saldo)
                    banco.adicionar_conta(conta)
                    messagebox.showinfo("Conta Criada", f"Conta Corrente criada para {titular} no banco {nome_banco} com saldo de {saldo:.2f}.")
                    self.destroy()
            else:
                messagebox.showerror("Erro", f"O cliente {titular} não foi encontrado no banco.")
        else:
            messagebox.showerror("Erro", f"O banco {nome_banco} não foi encontrado.")
