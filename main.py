from tkinter import *
from tkinter import ttk

# cores
gray = "#2F2E2E"
light_gray = "#E3E3E3"
orange = "#FE9D36"
white = "#FFFFFF"

# fontes

font_botao = "ivy 11 bold"
font_numeros_tela = "ivy 20"

# janela
janela = Tk()
janela.title("calculadora")
janela.geometry("350x490")

# dividindo a calculadora com frames
frame_tela = Frame(janela, width=350, height=65, bg=gray)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=350, height=435)
frame_corpo.grid(row=1, column=0)

# criando label

app_label = Label(
    frame_tela,
    text="1234567890",
    width=21,
    height=2,
    padx=7,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=font_numeros_tela,
    bg=gray,
    fg=white,
)
app_label.place(x=0, y=0)
# criando botões
b_c = Button(
    frame_corpo,
    text="C",
    width=18,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
    overrelief=RIDGE,
)
b_c.place(x=0, y=0)
b_por_cent = Button(
    frame_corpo,
    text="%",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
    overrelief=RIDGE,
)
b_por_cent.place(x=171, y=0)
b_divisao = Button(
    frame_corpo,
    text="/",
    width=9,
    height=4,
    bg=orange,
    fg=white,
    font=font_botao,
    relief=RAISED,
    overrelief=RIDGE,
)
b_divisao.place(x=261, y=0)

b_7 = Button(
    frame_corpo,
    text="7",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_7.place(x=0, y=85)
b_8 = Button(
    frame_corpo,
    text="8",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_8.place(x=85.5, y=85)
b_9 = Button(
    frame_corpo,
    text="9",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_9.place(x=171, y=85)
b_multiplicacao = Button(
    frame_corpo,
    text="x",
    width=9,
    height=4,
    bg=orange,
    fg=white,
    font=font_botao,
    relief=RAISED,
)
b_multiplicacao.place(x=261, y=85)

b_4 = Button(
    frame_corpo,
    text="4",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_4.place(x=0, y=170)
b_5 = Button(
    frame_corpo,
    text="5",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_5.place(x=85.5, y=170)
b_6 = Button(
    frame_corpo,
    text="6",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_6.place(x=171, y=170)
b_subtracao = Button(
    frame_corpo,
    text="-",
    width=9,
    height=4,
    bg=orange,
    fg=white,
    font=font_botao,
    relief=RAISED,
)
b_subtracao.place(x=261, y=170)


b_1 = Button(
    frame_corpo,
    text="1",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_1.place(x=0, y=255)
b_2 = Button(
    frame_corpo,
    text="2",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_2.place(x=85.5, y=255)
b_3 = Button(
    frame_corpo,
    text="3",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_3.place(x=171, y=255)
b_adicao = Button(
    frame_corpo,
    text="+",
    width=9,
    height=4,
    bg=orange,
    fg=white,
    font=font_botao,
    relief=RAISED,
)
b_adicao.place(x=261, y=255)


b_0 = Button(
    frame_corpo,
    text="0",
    width=18,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_0.place(x=0, y=340)
b_virgula = Button(
    frame_corpo,
    text=",",
    width=9,
    height=4,
    bg=light_gray,
    font=font_botao,
    relief=RAISED,
)
b_virgula.place(x=171, y=340)
b_igualdade = Button(
    frame_corpo,
    text="=",
    width=9,
    height=4,
    bg=orange,
    fg=white,
    font=font_botao,
    relief=RAISED,
)
b_igualdade.place(x=261, y=340)

janela.mainloop()
