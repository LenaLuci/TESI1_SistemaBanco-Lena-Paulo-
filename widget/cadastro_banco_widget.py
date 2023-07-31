import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco

class CadastroBancoWidget(tk.Toplevel):
    def __init__(self, parent, lista_bancos):
        super().__init__(parent)
        self.title("Cadastrar Banco")
        self.geometry("400x250")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.lista_bancos = lista_bancos

        frame_principal = tk.Frame(self, width=400, height=200, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        labelvazia = tk.Label(frame_principal, text='', bg='#3366cc')
        labelvazia.pack(pady=5)

        label_nome = tk.Label(frame_principal, text="Nome do Banco:", bg='#3366cc')
        label_nome.pack()

        self.entry_nome = tk.Entry(frame_principal)
        self.entry_nome.pack(pady=3)

        label_juros = tk.Label(frame_principal, text="Juros (%):", bg='#3366cc')
        label_juros.pack()
        self.entry_juros = tk.Entry(frame_principal)
        self.entry_juros.pack(pady=3)

        label_desconto = tk.Label(frame_principal, text="Desconto (%):", bg='#3366cc')
        label_desconto.pack()
        self.entry_desconto = tk.Entry(frame_principal)
        self.entry_desconto.pack(pady=3)

        button_cadastrar = tk.Button(frame_principal, text="Cadastrar", command=self.cadastrar_banco)
        button_cadastrar.pack(pady=15)

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