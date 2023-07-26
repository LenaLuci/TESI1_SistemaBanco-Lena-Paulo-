import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco
from widget.criar_conta_widget import CriarContaWidget
from widget.atualizar_banco_widget import AtualizarBancoWidget
from widget.mostrar_contas_widget import MostrarContasWidget

def open_criar_conta_window():
    criar_conta_window = tk.Toplevel(root)
    criar_conta_window.title("Criar Conta")
    criar_conta_widget = CriarContaWidget(criar_conta_window, banco)

def open_atualizar_banco_window():
    atualizar_banco_window = tk.Toplevel(root)
    atualizar_banco_window.title("Atualizar Banco")
    atualizar_banco_widget = AtualizarBancoWidget(atualizar_banco_window, banco)

def open_mostrar_contas_window():
    mostrar_contas_window = tk.Toplevel(root)
    mostrar_contas_window.title("Mostrar Contas")
    mostrar_contas_widget = MostrarContasWidget(mostrar_contas_window, banco)

def main():
    global root
    root = tk.Tk()
    root.wm_iconbitmap('poggiebank.ico')
    root.title("PoggieBank - Seu porquinho virtual")

    banco = Banco(1, "Banco Exemplo")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Criar Conta", command=open_criar_conta_window)
    file_menu.add_command(label="Atualizar Banco", command=open_atualizar_banco_window)
    file_menu.add_command(label="Mostrar Contas", command=open_mostrar_contas_window)
    file_menu.add_separator()
    file_menu.add_command(label="Sair", command=root.quit)
    menu_bar.add_cascade(label="Operacoes", menu=file_menu)

    root.mainloop()

if __name__ == "__main__":
    main()
