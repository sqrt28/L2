
"""fcts de Sam"""

def ad(a,b):
    "additione a et b"
    return a + b

def puissance_de(n,elements):
    "renvoie les valeurs de n à la puiissance jusqua elements"
    l = list()
    for i in range(elements):
        l.append((n**i))
    return l
    
def n_paire(elements):
    "renvoie les nombres paires"
    l = list()
    for i in range(0,elements,2):
        l.append(i)
    return l