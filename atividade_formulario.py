import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("300x300")

def enviar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    escolaridade = entrada_escolaridade.get()
    area = entrada_area.get()
    if area == 1:
        area_text = "Chefe"
    else:
        area_text = "Funcionário"

    msg = f"Nome: {nome}\nIdade: {idade}\nEscolaridade: {escolaridade}\nÁrea de Atuação: {area_text}"
    messagebox.showinfo("Dados Enviados", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 20)).grid(pady=10)

#ENTRADA DE TEXTO
tk.Label(janela, text="Nome:", font=("Arial")).grid(row=1, column=0)
entrada_nome = tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=1,column=1)
tk.Label(janela, text="Idade:",font=("Arial")).grid(row=2,column=0)
entrada_idade = tk.Entry(janela, font=("Arial"))
entrada_idade.grid(row=2, column=1)

#Combobox
tk.Label(janela, text="Escolaridade:", font=("Arial")).grid(row=3,column=0)
entrada_escolaridade = ttk.Combobox(janela, values=["Ensino Fundamental", "Ensino Médio", "Ensino Técnico", "Ensino Superior"])
entrada_escolaridade.grid(row=3,column=1)

#Radio
entrada_area = tk.IntVar()
entrada_area = tk.IntVar()
tk.Label(janela, text="Área de Atuação:", font=("Arial")).grid(row=4, column=0)
tk.Radiobutton(janela, text="Chefe", font=("Arial"), value=1, variable=entrada_area)\
    .grid(row=4, column=1)
tk.Radiobutton(janela, text="Funcionário", font=("Arial"), value=2, variable=entrada_area)\
    .grid(row=5,column=1)

#BOTÃO ENVIAR
tk.Button(janela, text="Enviar", command=enviar).grid(row=6, column=1,pady=20)


janela.mainloop()