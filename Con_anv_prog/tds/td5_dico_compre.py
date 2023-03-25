#EXERCICE 1:
print("\n"+"EXERCICE1:"+"\n")

DBD = {1:("toto","titi",19,True),2:("Barbosa","Sam",20,False),3:("Mache","Ethan",19,False),4:("Hertos","pierre",36,False)}
#question1
DBDIndex = {i : j[0] for i,j in DBD.items()}
print(DBDIndex)

#question2
DnumIP = {i : j for i,j in DBDIndex.items() if i  % 2 != 0}
print(DnumIP)

#question3:
EnsIP = {j for i,j in DBDIndex.items() if i  % 2 != 0}
print(EnsIP)

#EXERCICE 2:
print("\n"+"EXERCICE2:"+"\n")
stock = {"pelles" : 50, "marteau" : 100, "couteau" : 20,"verres" : 0}

#question1
def nombre_lots(nbreElem, taille_lot):
    return nbreElem // taille_lot

#question2
print("question2:")
commande = ["pelles","marteau","couteau","verres"]   

dico_res = {}
for i in commande:
    if i in stock:
        dico_res[i] = nombre_lots(stock[i],8)
    else:
        dico_res[i] = 0
res = {}
for nom in commande:
    nb_elements = stock.get(nom,0)
    nb_lots = nombre_lots(nb_elements,8)
    if nb_lots:
        res[nom] = nb_lots

#question3
print("question3:")
dico_res2 = {i : nombre_lots(stock.get(i,0),8) for i in commande}
print(dico_res2)

#question4
print("question4:")
dico = {i:j for i in commande if (j := nombre_lots(stock.get(i,0),8))}
print(dico)
correction = {nom : nb_lots for nom in commande if (nb_lots := nombre_lots(stock.get(nom,0),8))}
print(correction)
    
#question5
print("question5:")
gen = ((nom,nb_lots) for nom in commande if (nb_lots := nombre_lots(stock.get(nom,0),8)))
print(list(gen))

#EXERCICE3:
print("\n"+"EXERCICE3:"+"\n")
l =[0,0,1,2,3,3,2,4]

#question1
print("quetion1")

def frequence(liste):
    d = {}
    for i in liste:
        if i in d:
            d[i] += 1
        else:
            d[i]=1
    return d

def frequences_compre(liste):
    return{i : liste.count(i) for i in set(liste)} #set n'est pas obligatoire
frequences_compre(l)
print(frequence(l))

#question2
print("question2")

def supprime_doublons(dico):
    l = list()
    for i in dico.keys():
        l.append(i)
    return l

def supprime_doublons_compre(d):
    return[i for i in d.keys()]

def supprime_doublons_V2(liste):
    for elem in (freq := frequence(liste)):
        for _ in range(freq[elem]-1):
            liste.remove(elem)
               

print(supprime_doublons_compre(frequences_compre(l)))

#qusetion3
print("question3")

def garde_unique(l):
    l = list()
    dict_frequences = frequence(l)
    for k,v in dict_frequences.items():
        if v == 1:
            l.append(k)
    return l

def garde_uniques(l):
    return[k for k,v in frequence(l).items() if v == 1]

print(garde_uniques(l))