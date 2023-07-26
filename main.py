from tkinter import *

from PIL import Image


class Banco:

    def __init__(self, master: Tk, numero, nome):
        self.janelaLogin = master
        self.janelaLogin.title('PoggieBank - Seu porquinho virtual')
        self.janelaLogin.geometry('500x500')
        self.janelaLogin.resizable(width=False, height=False)
        self.janelaLogin.__numero = numero
        self.janelaLogin.__nome = nome
        self.janelaLogin.__contas = []



        #  Janelas dependentes
        frm_login = Frame(self.janelaLogin, bg='#3366cc', width=500, height=500)
        frm_login.pack()
        label_login = Label(frm_login, text='Usuário', bg='#3366cc', foreground='black')
        label_login.place(x=144, y=331)
        entry_login = Entry(frm_login, width=20, bg='white', fg='black')
        entry_login.place(x=200, y=330)
        label_senha = Label(frm_login, text='Senha', bg='#3366cc', foreground='black')
        label_senha.place(x=150, y=362)
        entry_senha = Entry(frm_login, width=20, bg='white', fg='black')
        entry_senha.place(x=200, y=361)
        btn_logar = Button(frm_login, text='Entrar')
        btn_logar.place(x=175, y=405)
        btn_criarconta = Button(frm_login, text='Criar conta')
        btn_criarconta.place(x=260, y=405)

        self.imagem = PhotoImage(file='imagens/poggiebank logo 250x250.png')
        imagem_red = self.imagem.subsample(3, 3)
        lbl = Label(frm_login, image=self.imagem, bg='#3366cc')
        lbl.place(x=125, y=50)


numero = 1
nome = ''
banco = Tk()
janela = Banco(banco, numero, nome)
banco.wm_iconbitmap('imagens/poggiebank.ico')
banco.mainloop()
