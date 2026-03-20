import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Login")
janela.configure(background="red")

frame_campos = tk.Frame(janela)
frame_campos.grid(row=0, column=0, padx=20, pady=20)

#USUÁRIO
ttk.Label(frame_campos, text="Usuário").pack()
entrada_user = tk.Entry(frame_campos)
entrada_user.pack()

#SENHA
ttk.Label(frame_campos, text="Senha").pack()
entrada_senha = tk.Entry(frame_campos)
entrada_senha.pack()

#BOTÃO
def clicar():
    messagebox.showinfo("Sucesso!", "Login efetuado com sucesso!")

btn = ttk.Button(frame_campos, text="Login", command=clicar)
btn.pack(pady=10)


#IMAGEM
imagem = tk.PhotoImage(file="obama-obunga.png")
imagem_menor = imagem.subsample(2, 2) 
label_foto = tk.Label(janela, image=imagem_menor)
label_foto.grid(row=0, column=1, padx=20)

janela.mainloop()
