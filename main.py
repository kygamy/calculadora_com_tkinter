from tkinter import *
from tkinter import ttk

# cores
gray = "#2F2E2E"


# janela
janela = Tk()
janela.title("calculadora")
janela.geometry("350x490")

# dividindo a calculadora com frames
frame_tela = Frame(janela, width=350, height=65)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=435)
frame_corpo.grid(row=1, column=0)

# criando botões
b_c = Button(frame_corpo, text="C", width=24, height=5)
b_c.place(x=0, y=0)
b_por_cent = Button(frame_corpo, text="%", width=12, height=5)
b_por_cent.place(x=175, y=0)
b_divisao = Button(frame_corpo, text="÷", width=12, height=5)
b_divisao.place(x=262.5, y=0)

b_7 = Button(frame_corpo, text="7", width=12, height=5)
b_7.place(x=0, y=85)
b_8 = Button(frame_corpo, text="8", width=12, height=5)
b_8.place(x=87.5, y=85)
b_9 = Button(frame_corpo, text="9", width=12, height=5)
b_9.place(x=175, y=85)
b_multiplicacao = Button(frame_corpo, text="x", width=12, height=5)
b_multiplicacao.place(x=262.5, y=85)

b_4 = Button(frame_corpo, text="4", width=12, height=5)
b_4.place(x=0, y=170)
b_5 = Button(frame_corpo, text="5", width=12, height=5)
b_5.place(x=87.5, y=170)
b_6 = Button(frame_corpo, text="6", width=12, height=5)
b_6.place(x=175, y=170)
b_subtracao = Button(frame_corpo, text="-", width=12, height=5)
b_subtracao.place(x=262.5, y=170)


b_1 = Button(frame_corpo, text="1", width=12, height=5)
b_1.place(x=0, y=255)
b_2 = Button(frame_corpo, text="2", width=12, height=5)
b_2.place(x=87.5, y=255)
b_3 = Button(frame_corpo, text="3", width=12, height=5)
b_3.place(x=175, y=255)
b_adicao = Button(frame_corpo, text="+", width=12, height=5)
b_adicao.place(x=262.5, y=255)


b_0 = Button(frame_corpo, text="0", width=24, height=5)
b_0.place(x=0, y=340)
b_virgula = Button(frame_corpo, text=",", width=12, height=5)
b_virgula.place(x=175, y=340)
b_igualdade = Button(frame_corpo, text="=", width=12, height=5)
b_igualdade.place(x=262.5, y=340)

janela.mainloop()
