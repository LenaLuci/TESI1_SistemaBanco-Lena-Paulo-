import tkinter as tk
from tkinter import messagebox


class AtualizarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Atualizar Banco")
        self.geometry('300x300')
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.banco = banco

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        #  imagem = tk.PhotoImage(file='imagens/poggiebank logo 80 80.png')
        #  lbl_foto = tk.Label(frame_principal, image=imagem, bg='#3366cc')
        #  lbl_foto.pack()

        label_fill = tk.Label(frame_principal, text='\n\n\n\n', bg='#3366cc')
        label_fill.pack(anchor=tk.CENTER)

        label_numero_banco = tk.Label(frame_principal, text="Número do Banco:", bg='#3366cc')
        label_numero_banco.pack(anchor=tk.CENTER)

        self.entry_numero_banco = tk.Entry(frame_principal)
        self.entry_numero_banco.pack(anchor=tk.CENTER)

        label_nome_banco = tk.Label(frame_principal, text="Nome do Banco:", bg='#3366cc')
        label_nome_banco.pack(anchor=tk.CENTER)

        self.entry_nome_banco = tk.Entry(frame_principal)
        self.entry_nome_banco.pack(anchor=tk.CENTER)

        label_fill2 = tk.Label(frame_principal, text='\n', bg='#3366cc')
        label_fill2.pack(anchor=tk.CENTER)

        button_atualizar_banco = tk.Button(frame_principal, text="Atualizar Banco", command=self.atualizar_banco)
        button_atualizar_banco.pack(anchor=tk.CENTER)

    def atualizar_banco(self):
        novo_numero = self.entry_numero_banco.get()
        novo_nome = self.entry_nome_banco.get()

        self.banco.set_numero(novo_numero)
        self.banco.set_nome(novo_nome)

        messagebox.showinfo("Atualização do Banco", "Informações do banco atualizadas com sucesso!")
