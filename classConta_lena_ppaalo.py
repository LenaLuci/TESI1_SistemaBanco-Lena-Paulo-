from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Conta:

    def editar(self):
        item = self.tvw.selection()
        if len(item) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
        else:
            valores = self.tvw.item(item, 'values')
            self.top_editar = Toplevel()
            self.top_editar.grab_set()
            lbl_nome = Label(self.top_editar, text='Nome:')
            lbl_nome.grid(row=0, column=0)
            lbl_telefone = Label(self.top_editar, text='Telefone:')
            lbl_telefone.grid(row=1, column=0)
            lbl_email = Label(self.top_editar, text='E-mail:')
            lbl_email.grid(row=2, column=0)
            self.ent_nome = Entry(self.top_editar)
            self.ent_nome.grid(row=0, column=1)
            self.ent_nome.insert('end', valores[0])
            self.ent_telefone = Entry(self.top_editar)
            self.ent_telefone.grid(row=1, column=1)
            self.ent_telefone.insert('end', valores[1])
            self.ent_email = Entry(self.top_editar)
            self.ent_email.grid(row=2, column=1)
            self.ent_email.insert('end', valores[2])
            btn_confirmar = Button(self.top_editar, text='Confirmar', command=self.confirmar_edicao)
            btn_confirmar.grid(row=3, column=0, columnspan=2)

    def confirmar_edicao(self):
        nome = self.ent_nome.get()
        telefone = self.ent_telefone.get()
        email = self.ent_email.get()
        selecionado = self.tvw.selection()
        if nome == '' or telefone == '' or email == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            self.tvw.item(selecionado, values=(nome, telefone, email))
            self.top_editar.destroy()

    def excluir(self):
        tupla = self.tvw.selection()
        for item in tupla:
            self.tvw.delete(item)

    #  PARA FAZER:
    #  1. Colocar mais colunas no cadastro: "CPF", "ENDEREÇO", "SENHA 4 DIGITOS", SENHA 6 DIGITOS"
    #  2. Fazer uma validação para quando realizar um login, entrar na conta cadastrada
    def cadastrar(self):

        self.top_cadastrar = Toplevel()
        self.top_cadastrar.geometry('200x200')
        self.top_cadastrar.wm_iconbitmap('poggiebank.ico')
        self.top_cadastrar.grab_set()
        lbl_nome = Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        lbl_telefone = Label(self.top_cadastrar, text='Telefone:')
        lbl_telefone.grid(row=1, column=0)
        lbl_email = Label(self.top_cadastrar, text='E-mail:')
        lbl_email.grid(row=2, column=0)
        self.ent_nome = Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0, column=1)
        self.ent_telefone = Entry(self.top_cadastrar)
        self.ent_telefone.grid(row=1, column=1)
        self.ent_email = Entry(self.top_cadastrar)
        self.ent_email.grid(row=2, column=1)
        btn_confirmar = Button(self.top_cadastrar, text='Confirmar', command=self.confirmar_cadastro)
        btn_confirmar.grid(row=3, column=0, columnspan=2)

    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        telefone = self.ent_telefone.get()
        email = self.ent_email.get()
        if nome == '' or telefone == '' or email == '':
            messagebox.showinfo('Aviso', 'Por favor, todos os campos são obrigatórios.', parent=self.top_cadastrar)
        else:
            self.tvw.insert('', 'end', values=(nome, telefone, email))
            self.top_cadastrar.destroy()

    def __init__(self, master: Tk, numero, cliente, saldo):
        self.janelaconta = master
        self.conta__numero = numero
        self.conta__cliente = cliente
        self.conta__saldo = saldo
        self.janelaconta.geometry('800x400')
        self.janelaconta.title('Contas')
        self.janelaconta.resizable(width=False, height=False)

        self.frameconta = Frame(width=800, height=400, bg='#3366cc')
        self.frameconta.pack(fill=BOTH, expand=True)

        colunas = ('nome', 'telefone', 'email')
        self.tvw = ttk.Treeview(self.frameconta, columns=colunas, height=5, show='headings')
        self.tvw.place(x=100, y=100)
        # Cabeçalho
        self.tvw.heading('nome', text='Nome')
        self.tvw.heading('telefone', text='Telefone')
        self.tvw.heading('email', text='E-mail')
        # Colunas
        self.tvw.column('nome', minwidth=200, width=200)
        self.tvw.column('telefone', minwidth=100, width=100)
        self.tvw.column('email', minwidth=300, width=300)
        # Linhas

        self.tvw.insert('', 'end', values=['Admin', 'admin', 'admin@admin.com'])

        # Barra de rolagem
        scb = Scrollbar(self.frameconta, orient=VERTICAL, command=self.tvw.yview)
        scb.place(x=700, y=101, height=125)
        self.tvw.config(yscrollcommand=scb.set)
        # Botões
        frm_botoes = Frame(self.frameconta)
        frm_botoes.place(x=400, y=300, anchor=CENTER)
        btn_cadastrar = Button(frm_botoes, text='Cadastrar', command=self.cadastrar)
        btn_cadastrar.grid(row=0, column=0)
        btn_excluir = Button(frm_botoes, text='Excluir', command=self.excluir)
        btn_excluir.grid(row=0, column=1)
        btn_editar = Button(frm_botoes, text='Editar', command=self.editar)
        btn_editar.grid(row=0, column=2)


numero = 1
cliente = 2
saldo = 50

app = Tk()
app.wm_iconbitmap('poggiebank.ico')
janela = Conta(app, numero, cliente, saldo)
app.mainloop()
