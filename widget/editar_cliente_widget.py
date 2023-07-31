import tkinter as tk
from tkinter import messagebox

class EditarClienteWidget(tk.Toplevel):
    def __init__(self, parent, cliente):
        super().__init__(parent)
        self.title("Editar Cliente")
        self.geometry("400x200")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.cliente = cliente

        label_nome = tk.Label(self, text="Nome Completo:")
        label_nome.pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.insert(0, cliente.get_nome())
        self.entry_nome.pack()

        label_cpf = tk.Label(self, text="CPF:")
        label_cpf.pack()
        self.entry_cpf = tk.Entry(self, state="disabled")
        self.entry_cpf.insert(0, cliente.get_cpf())
        self.entry_cpf.pack()

        label_endereco = tk.Label(self, text="Endereço:")
        label_endereco.pack()
        self.entry_endereco = tk.Entry(self)
        self.entry_endereco.insert(0, cliente.get_endereco())
        self.entry_endereco.pack()

        button_salvar = tk.Button(self, text="Salvar", command=self.salvar_edicao)
        button_salvar.pack()

    def salvar_edicao(self):
        nome = self.entry_nome.get()
        endereco = self.entry_endereco.get()

        if not nome or not endereco:
            messagebox.showerror("Campos Vazios", "Por favor, preencha todos os campos.")
            return

        self.cliente.set_nome(nome)
        self.cliente.set_endereco(endereco)

        messagebox.showinfo("Edição Salva", "Os dados do cliente foram atualizados com sucesso!")
        self.destroy()
