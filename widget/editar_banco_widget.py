import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EditarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Editar Banco")
        self.geometry("400x300")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        self.banco = banco

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        labelvazia = tk.Label(frame_principal, text='', bg='#3366cc')
        labelvazia.pack(pady=15)

        label_nome = tk.Label(frame_principal, text="Nome do Banco:", bg='#3366cc')
        label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(frame_principal)
        self.entry_nome.pack()
        self.entry_nome.insert(0, banco.get_nome())

        label_juros = tk.Label(frame_principal, text="Taxa de Juros (%):", bg='#3366cc')
        label_juros.pack(pady=5)
        self.entry_juros = tk.Entry(frame_principal)
        self.entry_juros.pack()
        self.entry_juros.insert(0, f"{banco.get_juros() * 100:.2f}")

        label_desconto = tk.Label(frame_principal, text="Desconto (%):", bg='#3366cc')
        label_desconto.pack(pady=5)
        self.entry_desconto = tk.Entry(frame_principal)
        self.entry_desconto.pack()
        self.entry_desconto.insert(0, f"{banco.get_desconto() * 100:.2f}")

        button_atualizar = tk.Button(frame_principal, text="Atualizar", command=self.atualizar_banco)
        button_atualizar.pack(pady=15)

    def atualizar_banco(self):
        nome = self.entry_nome.get()
        juros = float(self.entry_juros.get()) / 100.0
        desconto = float(self.entry_desconto.get()) / 100.0

        if not nome:
            messagebox.showerror("Erro", "O nome do banco não pode estar vazio.")
            return

        self.banco.set_nome(nome)
        self.banco.set_juros(juros)
        self.banco.set_desconto(desconto)

        messagebox.showinfo("Atualização Efetuada", "Banco atualizado com sucesso!")
        self.destroy()
