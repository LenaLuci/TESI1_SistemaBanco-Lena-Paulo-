import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EditarBancoWidget(tk.Toplevel):
    def __init__(self, parent, banco):
        super().__init__(parent)
        self.title("Editar Banco")
        self.geometry("400x200")

        self.banco = banco

        label_nome = tk.Label(self, text="Nome do Banco:")
        label_nome.pack()
        self.entry_nome = tk.Entry(self)
        self.entry_nome.pack()
        self.entry_nome.insert(0, banco.get_nome())

        label_juros = tk.Label(self, text="Taxa de Juros (%):")
        label_juros.pack()
        self.entry_juros = tk.Entry(self)
        self.entry_juros.pack()
        self.entry_juros.insert(0, f"{banco.get_juros() * 100:.2f}")

        label_desconto = tk.Label(self, text="Desconto (%):")
        label_desconto.pack()
        self.entry_desconto = tk.Entry(self)
        self.entry_desconto.pack()
        self.entry_desconto.insert(0, f"{banco.get_desconto() * 100:.2f}")

        button_atualizar = tk.Button(self, text="Atualizar", command=self.atualizar_banco)
        button_atualizar.pack()

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
