#morpion

import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(height =300, width = 300, bg = "white")
canvas.grid()
player = "croix"
somme1,somme2,somme3 = 0,0,0

for i in range(3):
    for j in range(3):
        canvas.create_line(i*100,j*100,i*100,j*100+100,fill = "black")
        canvas.create_line(i*100,j*100,i*100+100,j*100,fill = "black")







def jeu(event):
    global player, nbre, liste_jeu,somme1,somme2 ,somme3
    nbre = 0
    while nbre < 9:
        if  0 < event.x < 100 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(0,0,100,100)
                player = "croix"
                somme1 +=1
                print(liste_jeu)
    
                
            else:
                canvas.create_line(0,0,100,100)
                canvas.create_line(100,0,0,100)
                player = "oval"
                somme1 +=2
                print(liste_jeu)
                
            
            nbre += 1
    
        if  100 < event.x < 200 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(100,0,200,100)
                player = "croix"
                somme1 += 1
                print(liste_jeu)
            else:
                canvas.create_line(100,0,200,100)
                canvas.create_line(200,0,100,100)
                player = "oval"
                somme1 += 2
                print(liste_jeu)

            nbre += 1
            

        if  200 < event.x < 300 and 0 < event.y < 100:
            if  player == "oval" :
                canvas.create_oval(200,0,300,100)
                player = "croix"
                somme1 += 1
                print(liste_jeu)
            else:
                canvas.create_line(200,0,300,100)
                canvas.create_line(300,0,200,100)
                player = "oval"
                somme1 += 2
                print(liste_jeu)
                
            nbre += 1


        if  0 < event.x < 100 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(0,100,100,200)
                player = "croix"
                somme2 += 1
                print(liste_jeu)
            
            else:
                canvas.create_line(0,100,100,200)
                canvas.create_line(100,100,0,200)
                player = "oval"
                somme2 += 2
                print(liste_jeu)
            
            nbre += 1
    
        if  100 < event.x < 200 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(100,100,200,200)
                player = "croix"
                somme2 += 1
                print(liste_jeu)
            else:
                canvas.create_line(100,100,200,200)
                canvas.create_line(200,100,100,200)
                player = "oval"
                somme2 += 2
                print(liste_jeu)

            nbre += 1
    
        if  200 < event.x < 300 and 100 < event.y < 200:
            if  player == "oval" :
                canvas.create_oval(200,100,300,200)
                player = "croix"
                somme2 += 1
                print(liste_jeu)
            else:
                canvas.create_line(200,100,300,200)
                canvas.create_line(300,100,200,200)
                player = "oval"
                somme2 += 2
                print(liste_jeu)

            nbre += 1

        if  0 < event.x < 100 and 200 < event.y < 300:
            if  player == "oval" :
                canvas.create_oval(0,200,100,300)
                player = "croix"
                somme3 += 1
                print(liste_jeu)
            else:
                canvas.create_line(0,200,100,300)
                canvas.create_line(100,200,0,300)
                player = "oval"
                somme3 += 2
                print(liste_jeu)
            nbre += 1
    
        if  100 < event.x < 200 and 200 < event.y < 300:
            if  player == "oval" :
                canvas.create_oval(100,200,200,300)
                player = "croix"
                somme3 += 1
                print(liste_jeu)
            else:
                canvas.create_line(100,200,200,300)
                canvas.create_line(200,200,100,300)
                player = "oval"
                somme3 += 2
                print(liste_jeu)
            nbre += 1
        
            
    
        if  200 < event.x < 300 and 200 < event.y < 300:
            if  player == "oval" :
                canvas.create_oval(200,200,300,300)
                player = "croix"
                somme3 += 1
                print(liste_jeu)
            else:
                canvas.create_line(200,200,300,300)
                canvas.create_line(300,200,200,300)
                player = "oval"
                somme3 += 2
                print(liste_jeu)
            
            nbre += 1
        print(nbre)

        
def verif():
    if somme1 == 3:
        return "gagner pour les ronds"
    if somme2 == 6:
        return "gagner pour les croix"
verif()




canvas.bind("<Button-1>", jeu)
window.mainloop()