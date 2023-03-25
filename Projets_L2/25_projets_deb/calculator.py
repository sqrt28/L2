import tkinter as tk

# fonctions


def b0x():
    global chaine
    label["text"] += "0"
    chaine += "0"


def b1x():
    global chaine
    label["text"] += "1"
    chaine += "1"


def b2x():
    global chaine
    label["text"] += "2"
    chaine += "2"


def b3x():
    global chaine
    label["text"] += "3"
    chaine += "3"


def b4x():
    global chaine
    label["text"] += "4"
    chaine += "4"


def b5x():
    global chaine
    label["text"] += "5"
    chaine += "5"


def b6x():
    global chaine
    label["text"] += "6"
    chaine += "6"


def b7x():
    global chaine
    label["text"] += "7"
    chaine += "7"


def b8x():
    global chaine
    label["text"] += "8"
    chaine += "8"


def b9x():
    global chaine
    label["text"] += "9"
    chaine += "9"


def b_addx():
    global chaine
    label["text"] += "+"
    chaine += "+"


def b_sousx():
    global chaine
    label["text"] += "-"
    chaine += "-"


def b_multx():
    global chaine
    label["text"] += "*"
    chaine += "*"


def b_divx():
    global chaine
    label["text"] += "/"
    chaine += "/"


def point():
    global chaine
    label["text"] += "."
    chaine += "."


def effacer():
    global chaine
    label["text"] = ""
    chaine = ""


def b_egalx():
    try:
        label["text"] = str(eval(chaine))
    except:
        label["text"] = "erreur"


# programme
fenetre = tk.Tk()
fenetre.title("calculatrice")
l = list()
chaine = ""
label = tk.Label(fenetre, text="")
label.grid(column=0, row=0, columnspan=4)

# éléments
b_add = tk.Button(fenetre, text="+", command=b_addx)
b_sous = tk.Button(fenetre, text="-", command=b_sousx)
b_mult = tk.Button(fenetre, text="*", command=b_multx)
b_div = tk.Button(fenetre, text="/", command=b_divx)
b0 = tk.Button(fenetre, text="0", command=b0x)
b1 = tk.Button(fenetre, text="1", command=b1x)
b2 = tk.Button(fenetre, text="2", command=b2x)
b3 = tk.Button(fenetre, text="3", command=b3x)
b4 = tk.Button(fenetre, text="4", command=b4x)
b5 = tk.Button(fenetre, text="5", command=b5x)
b6 = tk.Button(fenetre, text="6", command=b6x)
b7 = tk.Button(fenetre, text="7", command=b7x)
b8 = tk.Button(fenetre, text="8", command=b8x)
b9 = tk.Button(fenetre, text="9", command=b9x)
b_point = tk.Button(fenetre, text=".", command=point)
b_egal = tk.Button(fenetre, text="=", command=b_egalx)
b_effacer = tk.Button(fenetre, text="effacer", bg='red', command=effacer)

# placement des éléments
b_add.grid(column=0, row=1)
b_sous.grid(column=1, row=1)
b_mult.grid(column=2, row=1)
b_div.grid(column=3, row=1)
b1.grid(column=0, row=2)
b2.grid(column=1, row=2)
b3.grid(column=2, row=2)
b4.grid(column=3, row=2)
b5.grid(column=0, row=3)
b6.grid(column=1, row=3)
b7.grid(column=2, row=3)
b8.grid(column=3, row=3)
b9.grid(column=0, row=4)
b0.grid(column=1, row=4)
b_point.grid(column=2, row=4)
b_egal.grid(column=3, row=4)
b_effacer.grid(column=0, row=5, columnspan=4)

# boucle
fenetre.mainloop()
