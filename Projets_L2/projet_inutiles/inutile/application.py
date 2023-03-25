import tkinter as tk
from tkinter import *
import webbrowser

fenetre = tk.Tk()
fenetre.geometry("1280x720")
fenetre.title("app")
def open():
    webbrowser.open_new("https://www.amazon.fr")

def exit():
    quit()

l1 = tk.Label(text = "tuto créer une application",bg = "purple")
l1.grid(column = 0, row = 0, columnspan= 2)



bouton_quitter = tk.Button(text = "quitter", command= exit)
bouton = tk.Button(text = "amazon",command = open)
bouton_quitter.grid(column = 0, row = 2)
bouton.grid(column = 0, row = 1)

fenetre.mainloop()

