import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco
from widget.mostrar_banco_widget import MostrarBancoWidget
from widget.criar_conta_widget import CriarContaWidget
from widget.mostrar_contas_widget import MostrarContasWidget
from widget.cadastro_cliente_widget import CadastroClienteWidget
from widget.criar_banco_widget import CriarBancoWidget
from widget.mostrar_cliente_widget import MostrarClientesWidget
from tkinter import PhotoImage


def sair():
    resposta = messagebox.askyesno("Saindo da sessão", "Deseja encerrar a sessão atual?")
    if resposta is True:
        root.destroy()


def main():
    global root
    root = tk.Tk()
    root.wm_iconbitmap('poggiebank.ico')
    root.title("PoggieBank - Seu porquinho virtual")
    root.geometry('350x350')
    root.resizable(width=False, height=False)

    frame_principal = tk.Frame(width=300, height=300, bg='#3366cc')
    frame_principal.pack(fill=tk.BOTH, expand=True)

    imagem = PhotoImage(file='imagens/poggiebank logo 250x250.png')
    lbl = tk.Label(frame_principal, image=imagem, bg='#3366cc')
    lbl.place(x=60, y=20)

    lbl_titulobanco = tk.Label(text='PoggieBank', font='Arial', bg='#3366cc', fg='white')
    lbl_titulobanco.place(x=125, y=275)
    lbl_sloganbanco = tk.Label(text='O cofrinho virtual mais Pog do mundo', font='Arial, 10', bg='#3366cc', fg='white')
    lbl_sloganbanco.place(x=62, y=300)

    banco = Banco(1, "Banco Exemplo")

    cliente1 = banco.criar_cliente("Paulo", "12345678900", "Rio Branco, Acre")
    cliente2 = banco.criar_cliente("Leona", "98765432100", "Cruzeiro do Sul, Acre")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    bancos = tk.Menu(menu_bar, tearoff=0)
    cliente = tk.Menu(menu_bar, tearoff=0)
    contas = tk.Menu(menu_bar, tearoff=0)

    contas.add_command(label="Criar Conta", command=lambda: CriarContaWidget(root, banco))
    contas.add_command(label="Mostrar Contas", command=lambda: MostrarContasWidget(root, banco))

    cliente.add_command(label="Cadastrar Clientes", command=lambda: CadastroClienteWidget(root, banco))
    cliente.add_command(label="Listar Clientes", command=lambda: MostrarClientesWidget(root, banco))

    bancos.add_command(label="Cadastrar Bancos", command=lambda: CriarBancoWidget(root, banco))
    bancos.add_command(label="Mostrar Bancos", command=lambda: MostrarBancoWidget(root, banco))

    menu_bar.add_cascade(label="Bancos", menu=bancos)
    menu_bar.add_cascade(label='Clientes', menu=cliente)
    menu_bar.add_cascade(label="Contas", menu=contas)
    menu_bar.add_command(label="Sair", command=sair)

    # file_menu.bind('<Control-Button-1>', root.withdraw())

    root.mainloop()


if __name__ == "__main__":
    main()
