import tkinter as tk
from tkinter import messagebox
from cadastro_conta_widget import CadastroContaWidget
from atualizar_banco_widget import AtualizarBancoWidget
from mostrar_contas_widget import MostrarContasWidget
from banco import Banco

class BancoApp(tk.Tk):
    def __init__(self):
        print("BancoApp init")
        super().__init__()
        self.title("Sistema Bancário")
        self.geometry("400x300")

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        operations_menu = tk.Menu(menu_bar, tearoff=0)
        operations_menu.add_command(label="Nova Conta", command=self.open_new_account_window)
        operations_menu.add_command(label="Mostrar Contas", command=self.show_accounts)
        operations_menu.add_command(label="Atualizar Banco", command=self.open_update_window)
        operations_menu.add_separator()
        operations_menu.add_command(label="Sair", command=self.quit)

        menu_bar.add_cascade(label="Operações", menu=operations_menu)

        self.banco = Banco(1, "Banco Exemplo")

    def open_new_account_window(self):
        print("Opening new account window")
        new_account_widget = CadastroContaWidget(self, self.banco)
        new_account_widget.grab_set()

    def open_update_window(self):
        update_widget = AtualizarBancoWidget(self, self.banco)
        update_widget.grab_set()

    def show_accounts(self):
        show_accounts_widget = MostrarContasWidget(self, self.banco)
        show_accounts_widget.grab_set()

if __name__ == "__main__":
    app = BancoApp()
    app.mainloop()
