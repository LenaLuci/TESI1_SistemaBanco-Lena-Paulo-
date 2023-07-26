import tkinter as tk
from tkinter import messagebox
from conta.conta import Conta
from cliente.cliente import Cliente


class CadastroContaWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Nova Conta")
        self.geometry('200x300')
        self.banco = banco

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        self.wm_iconbitmap('poggiebank.ico')

        label_fill = tk.Label(frame_principal, text='\n\n', bg='#3366cc')
        label_fill.pack(anchor=tk.CENTER)

        label_nome_cliente = tk.Label(frame_principal, text="Nome do Cliente:", bg='#3366cc')
        label_nome_cliente.pack()

        self.entry_nome_cliente = tk.Entry(frame_principal)
        self.entry_nome_cliente.pack()

        label_endereco = tk.Label(frame_principal, text="Endereço:", bg='#3366cc')
        label_endereco.pack()

        self.entry_endereco = tk.Entry(frame_principal)
        self.entry_endereco.pack()

        label_cpf = tk.Label(frame_principal, text="CPF:", bg='#3366cc')
        label_cpf.pack()

        self.entry_cpf = tk.Entry(frame_principal)
        self.entry_cpf.pack()

        label_saldo_inicial = tk.Label(frame_principal, text="Saldo Inicial:", bg='#3366cc')
        label_saldo_inicial.pack()

        self.entry_saldo_inicial = tk.Entry(frame_principal)#, state="disabled")
        self.entry_saldo_inicial.pack()

        label_fill2 = tk.Label(frame_principal, text='\n', bg='#3366cc')
        label_fill2.pack(anchor=tk.CENTER)

        button_cadastrar = tk.Button(frame_principal, text="Cadastrar", command=self.cadastrar_conta)
        button_cadastrar.pack()

    def cadastrar_conta(self):
        nome_cliente = self.entry_nome_cliente.get()
        endereco = self.entry_endereco.get()
        cpf = self.entry_cpf.get()
        saldo_inicial = self.entry_saldo_inicial.get()

        novo_cliente = Cliente(nome_cliente, endereco, cpf)

        nova_conta = Conta(len(self.banco.obter_contas()) + 1, novo_cliente, float(saldo_inicial))

        self.banco.adicionar_conta(nova_conta)

        messagebox.showinfo("Cadastro de Conta", f"Conta cadastrada:\nNome do Cliente: {nome_cliente}\nEndereço: {endereco}\nCPF: {cpf}\nSaldo Inicial: {saldo_inicial}")

        self.destroy()