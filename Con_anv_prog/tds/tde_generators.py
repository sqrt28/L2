from itertools import islice
#Exerice 1:

def entiers(n):
    for i in range(1,n):
        yield i
        
        
def carres(seq):
    for ele in seq:
        yield ele*ele 
        
def negatifs(seq):
    for ele in seq:
        if ele < 0:
            yield ele

flux = negatifs(carres(entiers(9)))
#next(flux)


#Exercice 2:

def fibon(n):
    a = 0
    b = 1
    resultat = list()
    for elem in range(n):
        resultat.append(a)
        a,b = b, a+b
    return resultat
print(fibon(5))

def fibonG(n):
    b = 1
    a = 0
    for elem in range(n):
        yield a
        a,b = b, a+b
    
a = fibonG(10)
print(list(a))


def fibon_rec(n):
    if n <=1:
        return n
    else: return fibon_rec(n-1) +fibon_rec(n-2)
    
    
def fibon_1(n):
    if n  >= 2:
        fct = [0,1]
        for i in range(2,n+1):
            fct.append(fct[i-1]+fct[i-2])
        return fct
    else:
        return [0,1][:n]

print(fibon_1(1))

#EXERCICE 3:
print("Exerice3")
#question1

text = "Je vais bien"

def indices_mots(text):
    resultat = list()
    for indice,val in enumerate(text):
        if indice == 0:
            print(0)
        if val == " ":
            print(indice+1)
print("question1:")
indices_mots(text)


#question 2 et 3:

text2 = "Four score seven years ago our fathers brought forth, upon a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal"

def indices_mots_gen(text):
    for indice, val in enumerate(text):
        if indice == 0:
            yield 0
        if val == " ":
            yield indice+1

print("question2/3:")
a = list(indices_mots_gen(text2))
print(a[:10])


#question 4:

def indice_fichier(lignes):
    cpt = 0
    for ligne in lignes:
        l = list(ligne)
        for i in  range(len(l)):
            if l[i] == " ":
                yield i 
                

def gen_fich(lignes):
    cpt = 0
    for ligne in lignes:
        for c in range(len(ligne)):
            if ligne[c] == " ":
                yield cpt+1
            cpt+=1
            
#correction
def gen_fichier_correction(fichier):
    offset = 0
    for ligne in fichier:
        if ligne:
            yield offset
            for carac in ligne:
                offset += 1
                if carac == " ":
                    yield offset       
                            

#questiton5
print("question4/5:")
with open("/Users/sambarbosa/visual_studio_code/L2/Con_anv_prog/tds/test_ex3.txt",'r') as fd:
        ite1= gen_fichier_correction(fd)

        ite2 =islice(ite1,0,10)
        print(list(ite2))


#Exercice4

matrix_A = [[0,2],[0,5]]
matrix_B = [[0,1],[8,6]]
matrix_C = [[0,0],[0,0]]


def somme_matrix(matrix1, matrix2,matrix_3):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix_3[i][j] = (matrix1[i][j]+ matrix2[i][j])
    
    return matrix_3

print(somme_matrix(matrix_A,matrix_B,matrix_C))


def ele_pairs(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 != 0:
                matrix[i][j] = 0
    return matrix

print(ele_pairs(matrix_C))


matrix_C = [ [matrix_A[i][j]+ matrix_B[i][j] for j in range(len(matrix_A[i]))] for i in range(len(matrix_A))]
print(matrix_C)
