import tkinter
from tkinter import *
from tkinter import ttk


# ------------------------ criando janela ------------------------

janela = Tk()
janela.title('')
janela.resizable(width=FALSE, height=FALSE)
janela.geometry('1100x550')

# ----------------------------------- cores -----------------------------------
cor0 = "#feffff"  # branco
cor_fundo = "#3a3a4d"  # azul fosco
cor_letra = "#030200"
cor1 = "#9c0c0c"
cor2 = "#0c9c41"
cor3 = "#0c909c"
cor4 = "#670c9c"
cor5 = "#140c9c"
cor6 = "#36354a"

# ----------------------------------- frames -----------------------------------

frame_app_nome = Frame(janela, width=1365, height=45, pady=0, padx=0, bg=cor0, relief='flat')
frame_app_nome.grid(row=0, column=0)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, column=1, ipadx=680)

frame_quadros = Frame(janela, width=1365, height=500, pady=10, padx=10, bg=cor_fundo, relief='flat')
frame_quadros.grid(row=3, column=0, sticky=NW)

# -----------------------------------  Nome do AP -----------------------------------

app_nome = Label(frame_app_nome, text="Dashboard COVID-19", width=32, height=2, pady=5, padx=0, bg=cor0, fg=cor_letra,
                 relief="flat", anchor="nw", font='Ivy 17 bold')
app_nome.place(x=0, y=10)

# -----------------------------------  Nome do AP -----------------------------------

frame_Total = Frame(frame_quadros, width=178, height=70, bg=cor0, relief="flat")
frame_Total.place(x=0, y=0)
app_pr = Label(frame_Total, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 1 bold', bg=cor2, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_Total, text="Total de casos", height=1, pady=0,
                     padx=0, relief="flat", anchor=CENTER, font='Ivy 10 bold', bg=cor0, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_Total, text="1234567", height=1, pady=0, padx=0,
                    relief="flat", anchor=CENTER, font='Roboto 16 ', bg=cor0, fg="#202124")
app_nome_va.place(x=10, y=35)

frame_recuperados = Frame(frame_quadros, width=178, height=70,
                          bg=cor0, relief="flat",)
frame_recuperados.place(x=188, y=0)
app_pr = Label(frame_recuperados, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 1 bold', bg=cor3, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_recuperados, text="Total Recuperado", height=1,
                     pady=0, padx=0, relief="flat", anchor=CENTER, font='Ivy 10 bold', bg=cor0, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_recuperados, text="1234567", height=1, pady=0,
                    padx=0, relief="flat", anchor=CENTER, font='Roboto 16 ', bg=cor0, fg="#202124")
app_nome_va.place(x=10, y=35)


frame_mortes = Frame(frame_quadros, width=178, height=70,
                     bg=cor0, relief="flat",)
frame_mortes.place(x=375, y=0)
app_pr = Label(frame_mortes, text="", width=1, height=10,
               pady=0, padx=0, relief="flat", anchor=NW, font='Ivy 1 bold', bg=cor4, fg=cor_letra)
app_pr.place(x=0, y=0)
app_nome_rev = Label(frame_mortes, text="Morte Total", height=1,
                     pady=0, padx=0, relief="flat", anchor=CENTER, font='Ivy 10 bold', bg=cor0, fg=cor_letra)
app_nome_rev.place(x=10, y=5)
app_nome_va = Label(frame_mortes, text="1234567", height=1, pady=0,
                    padx=0, relief="flat", anchor=CENTER, font='Roboto 16 ', bg=cor0, fg="#202124")
app_nome_va.place(x=10, y=35)

janela.mainloop()
