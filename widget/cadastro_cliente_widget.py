import tkinter as tk
from tkinter import messagebox
from cliente.cliente import Cliente

class CadastroClienteWidget(tk.Toplevel):
    def __init__(self, parent, banco, lista_clientes):
        super().__init__(parent)
        self.title("Cadastrar Cliente")
        self.geometry("400x200")

        self.banco = banco
        self.lista_clientes = lista_clientes

        label_nome = tk.Label(self, text="Nome Completo:")
        label_nome.pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()

        label_cpf = tk.Label(self, text="CPF:")
        label_cpf.pack()
        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.pack()

        label_endereco = tk.Label(self, text="Endereço:")
        label_endereco.pack()
        self.entry_endereco = tk.Entry(self)
        self.entry_endereco.pack()

        button_cadastrar = tk.Button(self, text="Cadastrar", command=self.cadastrar_cliente)
        button_cadastrar.pack()

    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()

        if len(cpf) != 11:
            messagebox.showerror("Erro", "O CPF deve ter 11 dígitos.")
            return
    
        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                messagebox.showerror("Erro", "CPF já cadastrado.")
                return

        cliente = Cliente(nome, cpf, endereco)
        self.lista_clientes.append(cliente)
        messagebox.showinfo("Cadastro Efetuado", "Cliente cadastrado com sucesso!")
        self.destroy()
