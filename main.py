import tkinter as tk
from banco.banco import Banco
from cliente.cliente import Cliente
from conta.conta import Conta
from widget.criar_conta_widget import CriarContaWidget
from widget.atualizar_banco_widget import AtualizarBancoWidget
from widget.mostrar_contas_widget import MostrarContasWidget
from widget.cadastro_conta_widget import CadastroContaWidget

def main():
    root = tk.Tk()
    root.wm_iconbitmap('poggiebank.ico')
    root.title("PoggieBank - Seu porquinho virtual")

    banco = Banco(1, "Banco Exemplo")

    criar_conta_widget = CriarContaWidget(root, banco)
    atualizar_banco_widget = AtualizarBancoWidget(root, banco)
    mostrar_contas_widget = MostrarContasWidget(root, banco)
    cadastro_conta_widget = CadastroContaWidget(root, banco)

    root.mainloop()

if __name__ == "__main__":
    main()
