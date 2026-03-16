import tkinter as tk

janela_main = tk.Tk()

janela_main.title("Oh o bixo piruleta")
janela_main.configure(background="white")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

#objetos em janela
tk.Label(janela_main, 
         text="Hello World",
         bg="white",
         font=("Arial", 30)
         ).pack()

tk.Label(janela_main,
         text="Caio Henrique",
         bg="white",
         font=("Arial", 20)
         ).pack()

#Imagens
imagem = tk.PhotoImage(file="obama-obunga.png")
imagem =imagem.subsample(1,1)
tk.Label(janela_main, image=imagem).pack()




janela_main.mainloop()