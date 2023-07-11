import tkinter as tk

#  def cadastrar(self):

class Banco:

    def __init__(self, master: tk.Tk, numero, nome):
        self.janelaLogin = master
        self.janelaLogin.title('Poggie Bank')
        self.janelaLogin.geometry('500x500')
        self.janelaLogin.resizable(width=False, height=False)
        self.janelaLogin.__numero = numero
        self.janelaLogin.__nome = nome
        self.janelaLogin.__contas = []

        #  Janelas dependentes
        frm_login = tk.Frame(self.janelaLogin, bg='#3366cc', width=500, height=500)
        frm_login.pack()
        label_login = tk.Label(frm_login, text='Usuário', bg='#3366cc', foreground='black')
        label_login.place(x=140, y=201)
        entry_login = tk.Entry(frm_login, width=20, bg='white', fg='black')
        entry_login.place(x=200, y=200)
        label_senha = tk.Label(frm_login, text='Senha', bg='#3366cc', foreground='black')
        label_senha.place(x=150, y=232)
        entry_senha = tk.Entry(frm_login, width=20, bg='white', fg='black')
        entry_senha.place(x=200, y=231)
        btn_logar = tk.Button(frm_login, text='Entrar')
        btn_logar.place(x=175, y=275)
        btn_criarconta = tk.Button(frm_login, text='Criar conta')
        btn_criarconta.place(x=260, y=275)
#  class Conta:
#
#    def __init__(self):
#        #  asd
#
#  class Cliente:
#
#    def __init__(self):
#        #  asdasd


numero = 1
nome = ''
banco = tk.Tk()
janela = Banco(banco, numero, nome)
banco.wm_iconbitmap('poggiebank.ico')
banco.mainloop()
