from tkinter import *
from PIL import Image, ImageTk


class MenuPrincipal:

    def cadastrar(self):
        self.janela_menu.deiconify()
        import classConta_lena_ppaalo

    def entrar(self):
        self.janela_menu.deiconify()
        import classBanco_lena_ppaalo

    def __init__(self, master: Tk):
        self.janela_menu = master
        self.janela_menu.title('Menu de opções')
        self.janela_menu.geometry('300x300')
        self.janela_menu.resizable(width=False, height=False)

        self.frame_principal = Frame(width=300, height=300, bg='#3366cc')
        self.frame_principal.pack(fill=BOTH, expand=True)

        caminho_imagem = Image.open('poggiebank logo 250x250.png')
        imagem = caminho_imagem.resize((200, 200))
        imagem = ImageTk.PhotoImage(imagem)
        lbl = Label(self.frame_principal, image=imagem)
        lbl.place(x=50, y=20)

        lbl_titulobanco = Label(text='PoggieBank', font='Arial', bg='#3366cc', fg='white')
        lbl_titulobanco.place(x=105, y=225)
        lbl_sloganbanco = Label(text='O porquinho virtual mais Pog do mundo', font='Arial, 10', bg='#3366cc', fg='white')
        lbl_sloganbanco.place(x=37, y=250)

        # Adicionando o menu para selecionar as outras janelas
        self.menu_barra = Menu(self.janela_menu)

        self.menu_criar_conta = Menu(self.menu_barra, tearoff=0)
        self.menu_barra.add_cascade(label='Opções', menu=self.menu_criar_conta)
        self.menu_criar_conta.add_command(label='Criar conta', command=self.cadastrar)
        self.menu_criar_conta.add_command(label='Entrar', command=self.entrar)
        self.menu_criar_conta.add_separator()
        self.menu_criar_conta.add_command(label='Sair', command=self.janela_menu.destroy)

        self.janela_menu.config(menu=self.menu_barra)


app = Tk()
janela = MenuPrincipal(app)
app.wm_iconbitmap('poggiebank.ico')
app.mainloop()
