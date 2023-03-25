
from tkinter import *
import tkinter
window = tkinter.Tk()
window.geometry("640x480")
window.title("test")
menu_button = tkinter.Menubutton(window, text = "Menu déroulant")
menu_button.menu = Menu(menu_button)
menu_button["menu"] = menu_button.menu
mayoVar = IntVar()
ketchVar = IntVar()
menu_button.menu.add_checkbutton(label = "choix1", variable = mayoVar)
menu_button.menu.add_checkbutton(label = "choix2", variable = ketchVar)
menu_button.grid()


window.mainloop()


