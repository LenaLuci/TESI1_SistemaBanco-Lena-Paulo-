import tkinter as tk
from tkinter import messagebox

class CriarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Criar Banco")
        self.geometry('200x300')

        self.wm_iconbitmap('poggiebank.ico')

        self.banco = banco

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        label_fill = tk.Label(frame_principal, text='\n\n', bg='#3366cc')
        label_fill.pack(anchor=tk.CENTER)

        # Criacao de Banco, Numero, nome (taxa de saldo, deposito)
        label_numero_banco = tk.Label(frame_principal, text="Número:", bg='#3366cc')
        label_numero_banco.pack()
        self.entry_numero_banco = tk.Entry(frame_principal)
        self.entry_numero_banco.pack()
        # defini min 4, max 4, numero

        label_nome_banco = tk.Label(frame_principal, text="Nome:", bg='#3366cc')
        label_nome_banco.pack()
        self.entry_nome_banco = tk.Entry(frame_principal)
        self.entry_nome_banco.pack()

        label_juros_banco = tk.Label(frame_principal, text="Taxa de Juros:", bg='#3366cc')
        label_juros_banco.pack()
        self.entry_juros_banco = tk.Entry(frame_principal)
        self.entry_juros_banco.pack()

        label_desconto_banco = tk.Label(frame_principal, text="Taxa de Desconto:", bg='#3366cc')
        label_desconto_banco.pack()
        self.entry_desconto_banco = tk.Entry(frame_principal)
        self.entry_desconto_banco.pack()

        label_fill = tk.Label(frame_principal, text='\n', bg='#3366cc')
        label_fill.pack(anchor=tk.CENTER)

        button_atualizar_banco = tk.Button(frame_principal, text="Atualizar Banco", command=self.atualizar_banco)
        button_atualizar_banco.pack()

    def atualizar_banco(self):
        novo_numero = self.entry_numero_banco.get()
        novo_nome = self.entry_nome_banco.get()

        self.banco.set_numero(novo_numero)
        self.banco.set_nome(novo_nome)

        messagebox.showinfo("Atualização do Banco", "Informações do banco atualizadas com sucesso!")