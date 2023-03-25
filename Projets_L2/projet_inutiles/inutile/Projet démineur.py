#  Projet démineur
import tkinter as tk
import random as rd

window = tk.Tk()
window.title("démineur")
canvas = tk.Canvas(height= 1000,width=1000, bg = "white")
canvas.grid()

for i in range(10):
    for j in range(10):
        canvas.create_line(i*100,j*100,i*100,j*100+100,fill = "black")
        canvas.create_line(i*100,j*100,i*100+100,j*100,fill = "black")


matrice = []
for i in range(10):
    matrice.append([])
    for j in range(10):
        matrice[i].append(0)


def bombes():
    "ajoute des bombes en rouge (cercles rouges)"
    liste = [0,100,200,300,400,500,600,700,800,900]
    for i in range(10):
        a = rd.choice(liste)
        b = rd.choice(liste)
        while a == b:
             b = rd.choice(liste)
        canvas.create_oval(a,b,a+100,b+100,fill="red")
        #matrice[i][j] = 1
    #print(matrice)
bombes()


def affichage():
    "affiche plusieurs rectangle verts pour chaque case"
    global liste_rectangle_green
    liste_rectangle_green = []
    for i in range(10):
        for j in range(10):
            liste_rectangle_green.append(canvas.create_rectangle(i*100,j*100,i*100+100,j*100+100,fill = "green"))
affichage()

def clic(event):
    "si clic sur rectangle vert alors le carré disparait"
    a = canvas.find_closest(event.x,event.y,halo = 10)
    canvas.delete(a)
    
        

def chiffres():
    "ajoute des chiffres près des bombes"
    canvas.create_text((50, 50),text= "1",font = ("Arial Black",30),fill = "black")
chiffres()


def drapeau(event):
    b =  canvas.find_closest(event.x,event.y,halo = 10)
    canvas.itemconfigure(b, fill = "red")



def verif():
    pass



    






















canvas.bind("<Button-2>", drapeau)
canvas.bind("<Button-1>", clic)
window.mainloop()