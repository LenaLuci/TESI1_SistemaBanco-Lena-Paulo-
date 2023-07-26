import tkinter as tk
from tkinter import messagebox
from banco import Banco
from banco_app import BancoApp

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_iconbitmap('poggiebank.ico')
    banco = Banco(1, "Banco Exemplo")

    print("Creating BancoApp instance")
    app = BancoApp()
    print("BancoApp instance created")

    root.mainloop()
