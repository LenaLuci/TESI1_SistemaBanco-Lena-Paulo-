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


        self.imagem = PhotoImage(file='imagens/poggiebank logo 250x250.png')
        imagem_red = self.imagem.subsample(3, 3)
        lbl = Label(image=self.imagem, bg='#3366cc')
        lbl.place(x=125, y=50)


numero = 1
nome = ''
banco = Tk()
janela = Banco(banco, numero, nome)
banco.wm_iconbitmap('imagens/poggiebank.ico')
banco.mainloop()
