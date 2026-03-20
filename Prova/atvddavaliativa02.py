import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

janela = tk.Tk()
janela.title("Formulário")

def enviar():
    nome = entrada_nome.get()
    sobrenome = entrada_sbnome.get()
    datanasc = entrada_data.get()
    cpf = entrada_cpf.get()
    cep = entrada_cep.get()
    sexo = opcao.get()
    if sexo == 1:
        sexo_texto = "Masculino"
    else:
        sexo_texto = "Feminino"
    estado = combo_estado.get()
    cidade = entrada_cdd.get()

    msg = f"Nome: {nome}\nSobrenome: {sobrenome}\nData de Nascimento: {datanasc}\nCPF: {cpf}\nCep: {cep}\nEstado: {estado}\nCidade: {cidade}\nSexo: {sexo_texto}\n"
    messagebox.showinfo("Dados Enviados", msg)

tk.Label(janela, text="Formulário de Cadastro", font=("Arial", 20)).grid(pady=10)

#NOME
tk.Label(janela, text="Nome:", font=("Arial")).grid(row=1, column=0)
entrada_nome = tk.Entry(janela, font=("Arial"))
entrada_nome.grid(row=1,column=1)

#SOBRENOME
tk.Label(janela, text="Sobreome:", font=("Arial")).grid(row=2, column=0)
entrada_sbnome = tk.Entry(janela, font=("Arial"))
entrada_sbnome.grid(row=2,column=1)

#DATA NASCIMENTO
tk.Label(janela, text="Data de Nascimento:", font=("Arial")).grid(row=3, column=0)
entrada_data = tk.Entry(janela, font=("Arial"))
entrada_data.grid(row=3,column=1)

#CPF
tk.Label(janela, text="CPF:", font=("Arial")).grid(row=4, column=0)
entrada_cpf = tk.Entry(janela, font=("Arial"))
entrada_cpf.grid(row=4, column=1)

#CEP
tk.Label(janela, text="CEP:", font=("Arial")).grid(row=5, column=0)
entrada_cep = tk.Entry(janela, font=("Arial"))
entrada_cep.grid(row=5,column=1)

#SEXO
opcao = tk.IntVar()
tk.Label(janela, text="Sexo:", font=("Arial")).grid(row=6,column=0)
tk.Radiobutton(janela, text="Masculino", font=("Arial"), value=1, variable=opcao)\
    .grid(row=6, column=1)
tk.Radiobutton(janela, text="Feminino", font=("Arial"), value=2, variable=opcao)\
    .grid(row=7, column=1)
tk.Radiobutton(janela, text="Outro", font=("Arial"), value=3, variable=opcao)\
    .grid(row=8, column=1)

#ESTADO
tk.Label(janela, text="Estado: ",font=("Arial")).grid(row=9,column=0)
combo_estado = ttk.Combobox(janela, values=["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"])
combo_estado.grid(row=9, column=1)

#CIDADE
tk.Label(janela, text="Cidade:", font=("Arial")).grid(row=11, column=0)
entrada_cdd = tk.Entry(janela, font=("Arial"))
entrada_cdd.grid(row=11,column=1)

#BOTAO ENVIAR
tk.Button(janela, text="Enviar", command=enviar).grid(row=13, column=1, pady=20)

janela.mainloop()
