import tkinter as tk

janela = tk.Tk()
janela.geometry("400x400")
janela.title("Mover Elementos")

frame_formulario = tk.Frame(janela, background='blue', bd=3, relief='solid')
frame_formulario.place(x=200, y=200, anchor='center')

entrada_nome = tk.Entry(frame_formulario)
entrada_nome.pack()
texto = tk.Label(frame_formulario, text="Nome")

entrada_sbnome = tk.Entry(frame_formulario)
entrada_sbnome.pack()
texto_sb = tk.Label(frame_formulario, text="Sobrenome")
texto_sb.pack()

janela.mainloop()