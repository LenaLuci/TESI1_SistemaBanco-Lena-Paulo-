import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco
from cliente.cliente import Cliente
from widget.mostrar_bancos_widget import MostrarBancosWidget
from widget.criar_conta_widget import CriarContaWidget
from widget.mostrar_contas_widget import MostrarContasWidget
from widget.cadastro_cliente_widget import CadastroClienteWidget
from widget.cadastro_banco_widget import CadastroBancoWidget
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
    root.geometry('450x350')
    root.resizable(width=False, height=False)

    frame_principal = tk.Frame(width=300, height=300, bg='#3366cc')
    frame_principal.pack(fill=tk.BOTH, expand=True)

    imagem = PhotoImage(file='imagens/poggiebank logo 250x250.png')
    lbl = tk.Label(frame_principal, image=imagem, bg='#3366cc')
    lbl.place(x=100, y=20)

    lbl_titulobanco = tk.Label(text='PoggieBank', font='Arial', bg='#3366cc', fg='white')
    lbl_titulobanco.place(x=185, y=275)
    lbl_sloganbanco = tk.Label(text='O cofrinho virtual mais Pog do mundo', font='Arial, 10', bg='#3366cc', fg='white')
    lbl_sloganbanco.place(x=120, y=300)

    lista_bancos = []
    banco = Banco(1, "PoggieBank", 0.05, 0.01)
    lista_bancos.append(banco)

    lista_clientes = []

    cliente1 = Cliente("Paulo", "12345678900", "Rio Branco, Acre")
    cliente2 = Cliente("Leona", "98765432100", "Cruzeiro do Sul, Acre")
    lista_clientes.append(cliente1)
    lista_clientes.append(cliente2)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    bancos = tk.Menu(menu_bar, tearoff=0)
    cliente = tk.Menu(menu_bar, tearoff=0)
    contas = tk.Menu(menu_bar, tearoff=0)

    contas.add_command(label="Criar Conta", command=lambda: CriarContaWidget(root, lista_bancos, lista_clientes))
    contas.add_command(label="Mostrar Contas", command=lambda: MostrarContasWidget(root, lista_bancos))

    cliente.add_command(label="Cadastrar Clientes", command=lambda: CadastroClienteWidget(root, banco, lista_clientes))
    cliente.add_command(label="Listar Clientes", command=lambda: MostrarClientesWidget(root, banco, lista_clientes))

    bancos.add_command(label="Cadastrar Bancos", command=lambda: CadastroBancoWidget(root, lista_bancos))
    bancos.add_command(label="Mostrar Bancos", command=lambda: MostrarBancosWidget(root, lista_bancos))

    menu_bar.add_cascade(label="Bancos", menu=bancos)
    menu_bar.add_cascade(label='Clientes', menu=cliente)
    menu_bar.add_cascade(label="Contas", menu=contas)
    menu_bar.add_command(label="Sair", command=sair)

    root.mainloop()


if __name__ == "__main__":
    main()
