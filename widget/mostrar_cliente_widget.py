import tkinter as tk
from tkinter import ttk, messagebox
from widget.editar_cliente_widget import EditarClienteWidget


class MostrarClientesWidget(tk.Toplevel):
    def __init__(self, parent, banco, lista_clientes):
        super().__init__(parent)
        self.title("Mostrar Clientes")
        self.geometry("600x400")

        self.banco = banco
        self.lista_clientes = lista_clientes

        self.client_list = ttk.Treeview(self, columns=("Nome", "CPF", "Endereço"), show="headings")
        self.client_list.heading("Nome", text="Nome")
        self.client_list.column('Nome', minwidth=150, width=200)
        self.client_list.heading("CPF", text="CPF")
        self.client_list.column('CPF', minwidth=100, width=150)
        self.client_list.heading("Endereço", text="Endereço")
        self.client_list.column('Endereço', minwidth=200, width=250)
        self.client_list.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.populate_clients()

        button_editar = tk.Button(self, text="Editar Cliente", command=self.editar_cliente)
        button_editar.pack()

        delete_button = tk.Button(self, text="Excluir", command=self.excluir_cliente)
        delete_button.pack()

    def populate_clients(self):
        self.client_list.delete(*self.client_list.get_children())
        for cliente in self.lista_clientes:
            self.client_list.insert("", "end", values=(cliente.get_nome(), cliente.get_cpf(), cliente.get_endereco()))

    def editar_cliente(self):
        selected_item = self.client_list.selection()
        if not selected_item:
            messagebox.showwarning("Seleção Inválida", "Nenhum cliente selecionado.")
            return

        item_id = selected_item[0]
        cpf = self.client_list.item(item_id, "values")[1]
        cliente = None
        for c in self.lista_clientes:
            if c.get_cpf() == cpf:
                cliente = c
                break

        if cliente:
            editar_cliente_widget = EditarClienteWidget(self, cliente)
            editar_cliente_widget.wait_window()

            self.populate_clients()

    def excluir_cliente(self):
        selected_item = self.client_list.selection()
        if not selected_item:
            messagebox.showwarning("Seleção Inválida", "Nenhum cliente selecionado.")
            self.destroy()
            return

        item_id = selected_item[0]
        nome = self.client_list.item(item_id, "values")[0]

        resposta = messagebox.askyesno("Excluir Cliente", f"Deseja excluir o cliente '{nome}'?")
        if resposta:
            cpf = self.client_list.item(item_id, "values")[1]

        for cliente in self.lista_clientes:
            if cliente.get_cpf() == cpf:
                self.lista_clientes.remove(cliente)
                break

        self.populate_clients()

        messagebox.showinfo("Cliente Excluído", f"O cliente '{nome}' foi excluído com sucesso.")
        self.destroy()

