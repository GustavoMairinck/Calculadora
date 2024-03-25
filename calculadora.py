from tkinter import *
from tkinter import ttk


todos_valores = "" 


def entrar_valor(event):
    global todos_valores
 
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""


def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")



#colors
co1 = "#000000" #preto
co4 = "#ffa600" #laranja
co3 = "#ffffff" #branco
co2 = "#878787" #cinza

#Janela
app = Tk()
app.title('Calculadora')
app.geometry("235x318")
app.config(bg=co1)

valor_texto = StringVar()

#display
display_frame = Frame(app, width=235, height=50, bg=co2)
display_frame.grid(row=0, column=0)


app_scream = Label(display_frame,textvariable=valor_texto,width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)


#corpo da calculadora
body_frame = Frame(app, width=235, height=268)
body_frame.grid(row=1, column=0)


#botões

#linha1

b_1 = Button(body_frame,command = lambda: limpar_tela(), text="C", width=11, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,)
b_1.place(x=0, y=0)
b_2 = Button(body_frame,command = lambda: entrar_valor('%'), text="%", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(body_frame,command = lambda: entrar_valor('/'), text="/", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
 
#linha2
b_4 = Button(body_frame,command = lambda: entrar_valor('7'), text="7", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(body_frame,command = lambda: entrar_valor('8'), text="8", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(body_frame,command = lambda: entrar_valor('9'), text="9", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(body_frame,command = lambda: entrar_valor('*'), text="*", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
 
#linha3
b_8 = Button(body_frame,command = lambda: entrar_valor('4'), text="4", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(body_frame,command = lambda: entrar_valor('5'), text="5", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(body_frame,command = lambda: entrar_valor('6'), text="6", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(body_frame,command = lambda: entrar_valor('-'), text="-", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)
 
#linha4
b_12 = Button(body_frame,command = lambda: entrar_valor('1'), text="1", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(body_frame,command = lambda: entrar_valor('2'), text="2", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(body_frame,command = lambda: entrar_valor('3'), text="3", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(body_frame,command = lambda: entrar_valor('+'), text="+", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)
 
#linha5
b_16 = Button(body_frame,command = lambda: entrar_valor('0'), text="0", width=11, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(body_frame,command = lambda: entrar_valor('.'), text=".", width=5, height=2, bg=co3, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(body_frame,command = lambda: calcular(), text="=", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

app.mainloop()

