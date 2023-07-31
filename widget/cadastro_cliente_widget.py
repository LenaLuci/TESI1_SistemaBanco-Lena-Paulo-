import tkinter as tk
from tkinter import messagebox
from cliente.cliente import Cliente

class CadastroClienteWidget(tk.Toplevel):
    def __init__(self, parent, banco, lista_clientes):
        super().__init__(parent)
        self.title("Cadastrar Cliente")
        self.geometry("350x250")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.banco = banco
        self.lista_clientes = lista_clientes

        frame_principal = tk.Frame(self, width=400, height=200, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        labelvazia = tk.Label(frame_principal, text='', bg='#3366cc')
        labelvazia.pack(pady=5)

        label_nome = tk.Label(frame_principal, text="Nome Completo:", bg='#3366cc')
        label_nome.pack(pady=3)
        self.entry_nome = tk.Entry(frame_principal)
        self.entry_nome.pack(pady=3)

        label_cpf = tk.Label(frame_principal, text="CPF:", bg='#3366cc')
        label_cpf.pack()
        self.entry_cpf = tk.Entry(frame_principal)
        self.entry_cpf.pack(pady=3)

        label_endereco = tk.Label(frame_principal, text="Endereço:", bg='#3366cc')
        label_endereco.pack()
        self.entry_endereco = tk.Entry(frame_principal)
        self.entry_endereco.pack(pady=3)

        button_cadastrar = tk.Button(frame_principal, text="Cadastrar", command=self.cadastrar_cliente)
        button_cadastrar.pack(pady=15)

    def cadastrar_cliente(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        endereco = self.entry_endereco.get()

        if len(cpf) != 11:
            messagebox.showerror("Erro", "Insira um CPF válido.")
            return
    
        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                messagebox.showerror("Erro", "CPF já cadastrado.")
                return

        cliente = Cliente(nome, cpf, endereco)
        self.lista_clientes.append(cliente)
        messagebox.showinfo("Cadastro Efetuado", "Cliente cadastrado com sucesso!")
