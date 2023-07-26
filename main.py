import tkinter as tk
from tkinter import messagebox
from banco.banco import Banco
from widget.criar_conta_widget import CriarContaWidget
from widget.atualizar_banco_widget import AtualizarBancoWidget
from widget.mostrar_contas_widget import MostrarContasWidget
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

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Criar Conta", command=lambda: CriarContaWidget(root, banco))
    file_menu.add_command(label="Atualizar Banco", command=lambda: AtualizarBancoWidget(root, banco))
    file_menu.add_command(label="Mostrar Contas", command=lambda: MostrarContasWidget(root, banco))
    file_menu.add_separator()
    file_menu.add_command(label="Sair", command=sair)
    menu_bar.add_cascade(label="Operacoes", menu=file_menu)

    #file_menu.bind('<Control-Button-1>', root.withdraw())

    root.mainloop()


if __name__ == "__main__":
    main()
