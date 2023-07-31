import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from banco.banco import Banco
from widget.editar_banco_widget import EditarBancoWidget

class MostrarBancosWidget(tk.Toplevel):
    def __init__(self, parent, lista_bancos):
        super().__init__(parent)
        self.title("Mostrar Bancos")
        self.geometry("600x400")
        self.resizable(width=False, height=False)

        self.wm_iconbitmap('poggiebank.ico')

        frame_principal = tk.Frame(self, width=300, height=300, bg='#3366cc')
        frame_principal.pack(fill=tk.BOTH, expand=True)

        self.lista_bancos = lista_bancos

        self.banco_list = ttk.Treeview(frame_principal, columns=("Número", "Nome do Banco", "Taxa de Juros (%)", "Desconto (%)"), show="headings")
        self.banco_list.heading("Número", text="Número")
        self.banco_list.column('Número', minwidth=50, width=70)
        self.banco_list.heading("Nome do Banco", text="Nome do Banco")
        self.banco_list.column('Nome do Banco', minwidth=150, width=200)
        self.banco_list.heading("Taxa de Juros (%)", text="Taxa de Juros (%)")
        self.banco_list.column('Taxa de Juros (%)', minwidth=100, width=150)
        self.banco_list.heading("Desconto (%)", text="Desconto (%)")
        self.banco_list.column('Desconto (%)', minwidth=100, width=150)
        self.banco_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.populate_bancos()

        button_excluir = tk.Button(frame_principal, text="Excluir", command=self.excluir_banco)
        button_excluir.pack(side=tk.RIGHT, padx=10, pady=7)

        button_editar = tk.Button(frame_principal, text="Editar", command=self.editar_banco)
        button_editar.pack(side=tk.RIGHT, padx=10, pady=7)

    def populate_bancos(self):
        self.banco_list.delete(*self.banco_list.get_children())
        for banco in self.lista_bancos:
            self.banco_list.insert("", "end", values=(banco.get_numero(), banco.get_nome(), f"{banco.get_juros()*100:.2f}%", f"{banco.get_desconto()*100:.2f}%"))
    
    def excluir_banco(self):
        selected_item = self.banco_list.selection()
        if not selected_item:
            messagebox.showwarning("Seleção Inválida", "Nenhum banco selecionado.")
            return

        item_id = selected_item[0]
        index = int(item_id[1:])
        if 0 < index <= len(self.lista_bancos):
            resposta = messagebox.askyesno("Excluir Banco", "Deseja excluir o banco selecionado?")
            if resposta:
                banco = self.lista_bancos[index - 1]
                self.lista_bancos.remove(banco)
                self.populate_bancos()
                self.destroy()
        else:
            messagebox.showerror("Erro", "Banco não encontrado.")
            return

    def editar_banco(self):
        selected_item = self.banco_list.selection()
        if not selected_item:
            messagebox.showwarning("Seleção Inválida", "Nenhum banco selecionado.")
            return

        item_id = selected_item[0]
        index = int(item_id[1:])  # Extract the index from the item_id
        if 0 < index <= len(self.lista_bancos):  # Check if the index is within the valid range
            banco = self.lista_bancos[index - 1]  # Get the bank object to edit
            editar_banco_widget = EditarBancoWidget(self, banco)
        else:
            messagebox.showerror("Erro", "Banco não encontrado.")
            return

