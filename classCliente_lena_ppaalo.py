from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class Cliente:

    def disable_event(self):
        pass

    def sair(self):
        resposta = messagebox.askyesno('Logout', 'Deseja mesmo finalizar a sessão?')
        if resposta is True:
            self.janelacliente.withdraw()

    def __init__(self, master: Tk, nome, endereco, cpf):
        self.janelacliente = master
        self.cliente__nome = nome
        self.cliente__endereco = endereco
        self.cliente__CPF = cpf
        self.janelacliente.geometry('300x600')
        self.janelacliente.title('Área do Cliente')
        self.janelacliente.resizable(width=False, height=False)

        self.framecliente = Frame(width=300, height=600, bg='#3366cc')
        self.framecliente.pack(fill=BOTH, expand=True)

        # Setando um frame com multiplas abas
        self.tabfrm = ttk.Notebook(self.framecliente, width=250, height=300)
        self.tabfrm.place(x=22, y=25, anchor=NW)

        # Declarando e adicionando as abas ao frame
        aba1 = ttk.Frame(self.tabfrm)
        aba2 = ttk.Frame(self.tabfrm)
        self.tabfrm.add(aba1, text='Informações')
        self.tabfrm.add(aba2, text='Transferências')

        # Configurações da aba1
        cliente_nome = Entry(aba1, state=DISABLED)
        cliente_nome.pack()

        btn_sair = Button(self.framecliente, text="Sair", command=self.sair)
        btn_sair.place(x=140, y=500)

        self.janelacliente.protocol("WM_DELETE_WINDOW", self.disable_event)


app = Tk()
nome = ''
endereco = ''
cpf = 0
janela = Cliente(app, nome, endereco, cpf)
app.wm_iconbitmap('poggiebank.ico')
app.mainloop()
