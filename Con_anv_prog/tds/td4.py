#exercice 1: liste en compréhension
print("Exercice 1:"+ "\n")
#1)

def couples(n):
    return [(i,j) for i in range(1,n+1) for j in range(1,n+1)] 
couples(10)

#2)
def couplesDiv(n):
    return[(i,j)  for i in range(1,n) for j in range(1,n) if i % j == 0]
couples(4)

#3)

def couplesDivV2(n):
    l = list()
    for i in range(1,n):
        for j in range(1,n):
            if i % j == 0:
                l.append((i,j))
    return l
couplesDivV2(4)


#Exericice 2: liste en compréhension
print( "\n"+"Exercice 2:"+ "\n")

matrix_A = [[0,2],[0,5]]
matrix_B = [[0,1],[8,6]]
matrix_C = [[0,0],[0,0]]


def somme_matrix(matrix1, matrix2,matrix_3):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix_3[i][j] = (matrix1[i][j]+ matrix2[i][j])
    
    return matrix_3

somme_matrix(matrix_A,matrix_B,matrix_C)


def ele_pairs(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 != 0:
                matrix[i][j] = 0
    return matrix

ele_pairs(matrix_C)


matrix_C = [ [matrix_A[i][j]+ matrix_B[i][j] for j in range(len(matrix_A[i]))] for i in range(len(matrix_A))]
matrixCP = [[elem if elem % 2 == 0 else 0 for elem in ligne]for ligne in matrix_C]
vecteur2 =[ele_in_ele for ele in matrixCP for ele_in_ele in ele]
print(matrixCP)
print(vecteur2)


#Exercice 3: expressions génératrices implique génératueur
print( "\n"+"Exercice 3:"+ "\n")

n = 10
entiers = (elem for elem in range(1,n+1))
carres = (ele * ele for ele in entiers)
negatifs = (-ele for ele in carres if ele >0)
nec = negatifs
print(list(nec))



#Exercice 4:
print( "\n"+"Exercice 4:"+ "\n")

BDP = [("toto","titi",19,True),("Barbosa","Sam",20,False),("Mache","Ethan",19,False),("Hertos","pierre",36,False)]

def EnsCelibataire(base_de_donnee):
    print("\n"+"les noms des personnes célibataires:"+"\n")
    return{ (i[0]) for i in base_de_donnee if i[3] == False}
print(EnsCelibataire(BDP))

def EnsCelibataireV2(base_de_donnee):
    print("\n"+"les noms et prénomes des personnes célibataires:"+"\n")
    return{ (i[0],i[1]) for i in base_de_donnee if i[3] == False}
print(EnsCelibataireV2(BDP))

def EnsCelibatairesT(base_de_donnee):
    print("\n"+"les prénomes puis noms des personnes célibataires ayant moins de 35 ans:"+"\n")
    return{(i[1],i[0]) for i in base_de_donnee if i[3]== False and i[2]<=35}
print(EnsCelibatairesT(BDP))


def EnsCelibataireTV2(base_de_donnee):
    print("\n"+"les noms et prénomes des personnes célibataires ayant moins de 35 ans  V2:"+"\n")
    ens = set()
    for i in base_de_donnee:
        if i[3] == False and i[2]<= 35:
                ens.add((i[0], i[1]))    
    return ens

print(EnsCelibataireTV2(BDP))


                
#Exerice Bonus:
l =[0,0,1,2,3,3,2,4]

def frequences(liste):
    return{i : liste.count(i) for i in liste}
print(frequences(l))


def supprime_doublons(d):
    return[i for i in d.keys()]

print(supprime_doublons(frequences(l)))

def garde_uniques(d):
    return[k for k,v in d.items() if v == 1]

print(garde_uniques(frequences(l)))

    
    

    
    