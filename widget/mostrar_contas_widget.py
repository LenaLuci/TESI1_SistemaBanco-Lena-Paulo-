import tkinter as tk
from tkinter import ttk

class MostrarContasWidget(tk.Toplevel):
    def __init__(self, parent, lista_bancos):
        super().__init__(parent)
        self.title("Mostrar Contas")
        self.geometry("800x300")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.lista_bancos = lista_bancos

        frame_principal = tk.Frame(self, width=400, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        self.conta_list = ttk.Treeview(frame_principal, columns=("Número", "Banco", "Tipo de Conta", "Titular", "Saldo"), show="headings")
        self.conta_list.heading("Número", text="Número")
        self.conta_list.column('Número', minwidth=50, width=70)
        self.conta_list.heading("Banco", text="Banco")
        self.conta_list.column("Banco", minwidth=100, width=150)
        self.conta_list.heading("Tipo de Conta", text="Tipo de Conta")
        self.conta_list.column('Tipo de Conta', minwidth=150, width=200)
        self.conta_list.heading("Titular", text="Titular")
        self.conta_list.column('Titular', minwidth=150, width=200)
        self.conta_list.heading("Saldo", text="Saldo")
        self.conta_list.column('Saldo', minwidth=100, width=150)
        self.conta_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.populate_contas()

    def populate_contas(self):
        self.conta_list.delete(*self.conta_list.get_children())
        for banco in self.lista_bancos:
            for conta in banco.obter_contas():
                self.conta_list.insert("", "end", values=(banco.get_nome(), conta.get_numero(), conta.get_tipo_conta(), conta.get_titular().get_nome(), f"R$ {conta.get_saldo():.2f}"))