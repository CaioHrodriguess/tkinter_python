import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulario")
janela.geometry("300x300")

def enviar():
    nome = entrada_nome.get()
    estado = combo_estado.get()
    sexo = opc.get()

    if sexo == 1:
        sexo_texto = "Masculino"
    else:
        sexo_texto = "Feminino"

    msg = f"Nome: {nome}\nEstado: {estado}\nSexo: {sexo_texto}"
    messagebox.showinfo("Dados Enviados", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 20)).grid(pady=10)
#entrada de texto
tk.Label(janela, text="Nome:",  font=("Arial")).grid(row=1, column=0)
entrada_nome= tk.Entry(janela,font=("Papyrus"))
entrada_nome.grid(row=1, column=1)

#radiobutton
opc = tk.IntVar()

opc = tk.IntVar()
tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=2, column=0)
tk.Radiobutton(janela, text="Masculino", font=("Papyrus") ,value=1, variable=opc)\
    .grid(row=3, column=1)
tk.Radiobutton(janela, text="Feminino", font=("Papyrus") ,value=2, variable=opc)\
    .grid(row=4, column=1)

#COMBOBOX
tk.Label(janela, text="Estado").grid(row=6, column=0)
combo_estado = ttk.Combobox(janela, values=["MG", "SP", "RJ", "RN", "BA"])
combo_estado.grid(row=5, column=1)

#botão
tk.Button(janela, text="Enviar", command=enviar).grid(row=7, column=1,pady=20)

janela.mainloop()