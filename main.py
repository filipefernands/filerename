# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as tkmsg
import ProcessFiles as execProc

class Application:

    def __init__(self, master=None):

        # Definição da janela
        app.title("File Rename")
        app.iconbitmap('file.ico')
        app.resizable(0,0)

        # Color
        self.colorFont = "blue"

        # Container titutlo
        self.container_titulo = Frame(master)
        self.container_titulo.pack()

        # Container path
        self.container_path = Frame(master)
        self.container_path.pack(fill=X, padx=10)

        # Container prefix
        self.container_prefix = Frame(master)
        self.container_prefix.pack(fill=X, padx=10, pady=10)

        # Container buttons
        self.container_button = Frame(master)
        self.container_button.pack(padx=10, pady=10)


        # Label titulo
        self.lbTitulo = Label(self.container_titulo,text="::FILE RENAME::", padx=10, pady=10)
        self.lbTitulo.pack()

        # Label/Input path
        self.lbtPath = Label(self.container_path, text="Path:", width=5, anchor=S)
        self.lbtPath.pack(side=LEFT)
        self.txtPath = Entry(self.container_path, fg=self.colorFont)
        self.txtPath.pack(fill=X)

        #Label/Input prefix
        self.lbPrefix = Label(self.container_prefix, text="Prefix:", width=5, anchor=S)
        self.lbPrefix.pack(side=LEFT)
        self.txtPrefix = Entry(self.container_prefix, width=10, fg=self.colorFont)
        self.txtPrefix.pack(side=LEFT)

        # Label/Input tamanho prefix
        self.lbTamanhoPrefix = Label(self.container_prefix, text="Size:", width=5, anchor=S)
        self.lbTamanhoPrefix.pack(side=LEFT)
        self.txtTamanhoPrefix = Entry(self.container_prefix, width=10, fg=self.colorFont)
        self.txtTamanhoPrefix.pack(side=LEFT)

        # Buttons About/Process/Exit
        self.btnExit = Button(self.container_button, text="Exit", width=5, command=self.Exit)
        self.btnExit.pack(side=LEFT)
        self.btnAbout = Button(self.container_button, text="About", width=10, command=self.About)
        self.btnAbout.pack(side=LEFT, padx=5)
        self.btnProcess = Button(self.container_button, text="Process", width=10, command=self.IniProcess)
        self.btnProcess.pack()

        # Binding para executar a função que gera a quantidade de caracter do prefixo digitado
        self.txtPrefix.bind("<FocusOut>", self.PrefixSize)

    # Janela about
    @staticmethod
    def About():

        # Definição da janela
        about = Toplevel(app)
        about.title("About")
        about.iconbitmap("file.ico")
        about.resizable(0,0)

        # Centraliza a janela about ao centro da tela
        widtha = 300
        heighta = 120
        wsa = about.winfo_screenwidth()
        hsa = about.winfo_screenheight()
        widthxa = (wsa / 2) - (widtha / 2)
        heightya = (hsa / 2) - (heighta / 2)
        about.geometry('%dx%d+%d+%d' % (widtha, heighta, widthxa, heightya))

        # Define o about
        msg_about = "Aplicativo desenvolvido para renomear o prefixo das regras para abrir em outros módulos do sistema.\n\n Autor: Filipe Rocha - Versão 1.0"
        msg = Message(about, text=msg_about, width=280, anchor=CENTER)
        msg.config(font=('Arial', 10))
        msg.pack(fill=X, padx=10)

        # Button sair
        btnOK = Button(about, text="OK", height=0, width=10, command=about.destroy)  # kills one win
        btnOK.pack(padx=20)

    # Inicia o processo
    def IniProcess(self):

        # Validação dos campos
        if not self.txtPath.get():
            tkmsg.showwarning(title="Aviso", message="Informe o diretório dos arquivos!")
        elif not self.txtPrefix.get():
            tkmsg.showwarning(title="Aviso", message="Informe o prefixo do arquivo!")
        elif not self.txtTamanhoPrefix.get():
            tkmsg.showwarning(title="Aviso", message="Informe o tamanho do prefixo!")

        # Executa o processo
        executar = execProc.Files(self.txtPath.get(), self.txtPrefix.get(), self.txtTamanhoPrefix.get())

        if executar.ProcessFiles():
            tkmsg.showinfo(title="Info", message="Arquivos renomeados com sucesso!")
        else:
            tkmsg.showerror(title="Erro", message="Ocorreu um erro ao tentar renomear os arquivos.")

    # Gera a quantidade de caracter do prefixo ao ocorrer o evento FocusOut
    def PrefixSize(self, *args):
        self.txtTamanhoPrefix.delete(0, END)
        self.txtTamanhoPrefix.insert(0, len(self.txtPrefix.get()))

    # Fechar o aplicativo
    @staticmethod
    def Exit():
        app.destroy()

# Inicia o aplicativo
if __name__ == "__main__":
    app = Tk()
    # Centraliza a tela app.geometry("300x150")
    width = 300
    height = 150
    ws = app.winfo_screenwidth()
    hs = app.winfo_screenheight()
    widthx = (ws / 2) - (width / 2)
    heighty = (hs / 2) - (height / 2)
    app.geometry('%dx%d+%d+%d' % (width, height, widthx, heighty))
    Application(app)
    app.mainloop()