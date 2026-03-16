import tkinter as tk

janela_main = tk.Tk()

janela_main.title("Título")
janela_main.configure(background="pink")
janela_main.minsize(200,200)
janela_main.maxsize(500,500)
janela_main.geometry("300x300")

tk.Label(janela_main,
         text="Título",
         bg="white",
         font=("Arial", 30)
         ).pack()

tk.Label(janela_main,
         text="Etiqueta",
         bg="White",
         font=("Arial", 30)
         ).pack()

#Imagens
imagem = tk.PhotoImage(file="obama-obunga.png")
imagem =imagem.subsample(1,1)
tk.Label(janela_main, image=imagem).pack

tk.Label(janela_main,
         text="Cachorro Lascado",
         bg="Red",
         font=("Arial", 30)
         ).pack()

janela_main.mainloop()