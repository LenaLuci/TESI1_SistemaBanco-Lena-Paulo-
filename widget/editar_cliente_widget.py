import tkinter as tk
from tkinter import messagebox

class EditarClienteWidget(tk.Toplevel):
    def __init__(self, parent, cliente):
        super().__init__(parent)
        self.title("Editar Cliente")
        self.geometry("400x300")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.cliente = cliente

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        labelvazia = tk.Label(frame_principal, text='', bg='#3366cc')
        labelvazia.pack(pady=15)

        label_nome = tk.Label(frame_principal, text="Nome Completo:", bg='#3366cc')
        label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(frame_principal)
        self.entry_nome.insert(0, cliente.get_nome())
        self.entry_nome.pack()

        label_cpf = tk.Label(frame_principal, text="CPF:", bg='#3366cc')
        label_cpf.pack(pady=5)
        self.entry_cpf = tk.Entry(frame_principal, state="disabled")
        self.entry_cpf.insert(0, cliente.get_cpf())
        self.entry_cpf.pack()

        label_endereco = tk.Label(frame_principal, text="Endereço:", bg='#3366cc')
        label_endereco.pack(pady=5)
        self.entry_endereco = tk.Entry(frame_principal)
        self.entry_endereco.insert(0, cliente.get_endereco())
        self.entry_endereco.pack()

        button_salvar = tk.Button(frame_principal, text="Salvar", command=self.salvar_edicao)
        button_salvar.pack(pady=15)

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
