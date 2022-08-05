import tkinter
from tkinter import *
from tkinter import ttk
# ----------------------------------- matplotlib ----------------------------------------------------------------------

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# -----------------------------------------pandas e numpy--------------------------------------------------------------
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------------------------------------------------

from dados import *


# ----------------------------------- criando janela ----------------------------------

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
cores = [cor1, cor2, cor3, cor4, cor5, cor6]


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

# -----------------------------------  Top 5 países mais afetados -----------------------------------
frame_top = Frame(frame_quadros, width=200, height=500, bg=cor0, relief="flat",)
frame_top.place(x=560, y=0)

# obtendo valores de meses
lista_pais = ['Angola', "Portugal", 'Brazil', 'India']
lista_valores = [10002, 27265, 3826, 27125]


# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(8.7, 3), dpi=60)
ax = figura.add_subplot(111)

ax.barh(lista_pais, lista_valores,
        align='center', color=cores)
ax.set_alpha(0.3)

# set individual bar lables using above list
c = 0
# set individual bar lables using above list
for i in ax.patches:
    # get_width pulls left or right; get_y pushes up or down
    ax.text(i.get_width()+.3, i.get_y()+.50,
            # ={'weight':'bold'}
            str(lista_valores[c]), fontsize=12, verticalalignment='center', fontstyle='italic', weight='bold',
            color='dimgrey'
            )
    c += 1

# Axis formatting.
ax.patch.set_facecolor('#FFFFFF')
ax.spines['bottom'].set_color('#CCCCCC')
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(0)
ax.spines['top'].set_linewidth(0)
ax.spines['left'].set_color('#CCCCCC')
ax.spines['left'].set_linewidth(1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(False)
ax.xaxis.grid(False)


app_nome_rev = Label(frame_top, text="Top 5 países mais afetados", height=1,
                     pady=5, padx=0, relief="flat", anchor=NW, font='Ivy 10 bold', bg=cor0, fg=cor4)
app_nome_rev.grid(row=0, column=0, padx=20, pady=0, sticky=NSEW)
canva = FigureCanvasTkAgg(figura, frame_top)
canva.get_tk_widget().grid(row=1, column=0, sticky=NSEW, columnspan=2)

# ----------------------------------------------------- Paises ---------------------------------------------------

frame_paises = Frame(frame_quadros, width=700, height=500,
                     bg=cor0, relief="flat",)
frame_paises.place(x=0, y=80)

# este codigo serve para estilizar a tabela em Tkinter
style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading",
                background="#494d4a", foreground="white", relief="raised")
style.map("Custom.Treeview.Heading",
          relief=[('active', 'groove'), ('pressed', 'sunken')])


# cabeçalho da tabela
lista_head = ['País',  'Total Confirmado',
              'Total Recuperado', 'Total mortes', 'Data']

tree = ttk.Treeview(frame_paises, selectmode="extended", style="Custom.Treeview", height=18,
                    columns=lista_head, show="headings")
# vertical scrollbar
vsb = ttk.Scrollbar(
    frame_paises, orient="vertical", command=tree.yview)
# horizontal scrollbar
hsb = ttk.Scrollbar(
    frame_paises, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=1, sticky='nsew')
vsb.grid(column=1, row=1, sticky='ns')
hsb.grid(column=0, row=2, sticky='ew')
frame_paises.grid_rowconfigure(0, weight=2)


# definindo algumas propriedades para a tabela
hd = ["nw", "center", "center", "center", "center", "center", "center"]
h = [140, 100, 100, 100, 91]
n = 0

for col in lista_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n], anchor=hd[n])

    n += 1

'''
for item in lista_paizes:
    tree.insert('', 'end', values=item)
'''
# ------------------------------------------------Continente mais afetado-----------------------------------------------

frame_categoria = Frame(frame_quadros, width=200,
                        height=200, bg=cor0, relief="flat",)
frame_categoria.place(x=562, y=220)

lista_continentes_valor = [3568870, 27195616,
                           19517392, 22281680, 1794942, 19269056]
lista_continentes_nome = ['Africa', 'Asia', 'Europe',
                          'North-America', 'Oceania', 'South-America']


# faça figura e atribua objetos de eixo
figura = plt.Figure(figsize=(8.65, 3.9), dpi=60)
ax = figura.add_subplot(111)

colors = ['#5588bb', '#66bbbb', '#aa6644',
          '#99bb55', '#ee9944', '#444466', '#bb5555']

wedges, texts = ax.pie(lista_continentes_valor, wedgeprops=dict(
    width=0.2), colors=colors, shadow=True, startangle=-90)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(lista_continentes_nome[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

app_categoria = Label(frame_categoria, text="Continente mais afetado", height=1,
                      pady=5, padx=0, relief="flat", anchor=NW, font='Ivy 10 bold', bg=cor0, fg=cor4)
app_categoria.grid(row=0, column=0, pady=0,
                   padx=20, columnspan=2, sticky=NSEW)
canva_cont = FigureCanvasTkAgg(figura, frame_categoria)
canva_cont.get_tk_widget().grid(row=1, column=0, sticky=NSEW)


janela.mainloop()
