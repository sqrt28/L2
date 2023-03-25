#importations des modules et chargement du fichier de tweets
import json
import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import matplotlib.pyplot as plt

f = open("versailles_tweets_100.json","r")
data = json.load(f)

def supprime_emojis(val):
    message = ""
    for i in val:
        if re.compile("[\w|\.|,|\?|!|:|;|\s|(|)|\-|@|#|/|'|_|’]").search(i):
            message += i
    return message

# définition de la classe Tweet
class Tweet:
    def __init__(self, ecrivain, message, hashtags = "pas de hashtags", mention= "pas de mentions"):
        self.ecrivain = ecrivain
        self.mention = mention
        self.message = message
        self.hashtags = hashtags
        
    def find_hashtags(self):
        regex = re.compile("(#[A-Za-z][A-Za-z0-9-_]+)")
        self.hashtags = regex.findall(self.message)
        return self.hashtags
    
    def find_mention(self):
        regex = re.compile("(@[A-Za-z][A-Za-z0-9-_]+)")
        self.mention = regex.findall(self.message)
        return self.mention
    
    
    def affichage_auteur(self):
        return self.ecrivain
        
    def affichage_hashtag(self):
        return Tweet.find_hashtags(self)
    
    def affichage_mention(self):
        return Tweet.find_mention(self)
    
    def affichage_message(self):
        return self.message
    
    def sentiment_message(self):
        p = TextBlob(self.message,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer())
        if p.sentiment[0] > 0 :
            return("négatif")
        elif p.sentiment[0] < 0 :
            return("positif")
        else:
            return("neutre")
    
    def info(self):
        return self.ecrivain, self.message, Tweet.find_hashtags(self), Tweet.find_mention(self)

l_tweets = []     

for i in range(len(data)):
    for item, val in data[i].items():
        if item == "author_id":
            auteur = val
        if item == "text":
            message = supprime_emojis(val)
    l_tweets.append(Tweet(auteur,message))

filtrer = open("filtre.txt","w")
for i in range(len(l_tweets)):
    filtrer.write(str(l_tweets[i].info())+ "\n" + "\n")
filtrer.close()    
    
def Parcourir_tweet():
    print("il y a",len(l_tweets),"tweets en tout")
    c = 0
            
    while 1:
        c = input("quel tweet ?  ")
        while 1:
            try:
                c = int(c)
                break
            except:
                c = input("saisie non valide")
        print(l_tweets[c].affichage_message())
        while 1:
            n = input(" saississez un nombre: 0 = auteur de la publication, 1 = hashtags dans la publication, 2 = mentions dans la publication, 3 : sentiment du tweet ")
            while 1:
                    try:
                        n = int(n)
                        break
                    except:
                        n = input("saisie non valide : entrer 0, 1, 2, 3")
            if n == 0:
                print(l_tweets[c].affichage_auteur())
            if n == 1:
                print(l_tweets[c].affichage_hashtag())
            if n == 2:
                print(l_tweets[c].affichage_mention())
            if n == 3:
                print(l_tweets[c].sentiment_message())
            arret = input("voulez vous continuer? (oui ou non) ")
            if arret == "oui":
                pass
            elif arret == "non": 
                break
            else:
                pass
        other_tweet = input("analyser un autre tweet ? (oui ou non) ")
        if other_tweet == "oui":
            pass
        else:
            break
        
#top hashtags
l_hashtags = list()
for i in range(len(l_tweets)):
    l_hashtags.append(l_tweets[i].find_hashtags())

l_hashtags1 = list()
for i in range(len(l_hashtags)):
    for j in range(len(l_hashtags[i])):
        l_hashtags1.append(l_hashtags[i][j])
l_hashtags_count = list()
l_hashtags_final = list()
a = 0
for i in l_hashtags1:
    if i in l_hashtags_final:
        pass
    else:
        l_hashtags_final.append(l_hashtags1[a])
    a += 1
for i in range(len(l_hashtags_final)):
    l_hashtags_count.append(l_hashtags1.count(l_hashtags_final[i]))


l_top_hastags = list()
for i in range(len(l_hashtags_final)):
    l_top_hastags.append([l_hashtags_count[i],l_hashtags_final[i]])

def top_hastag(k):
    l = sorted(l_top_hastags, reverse =True)
    if k > len(l):
        k = len(l)
    l_f = []
    x = []
    y = []
    for i in range(k):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("hashtags")
    plt.ylabel("nbre apparition")
    plt.show()

def nombre_publication_hashtags():
    l = sorted(l_top_hastags, reverse =True)
    if k > len(l):
        k = len(l)
    l_f = []
    x = []
    y = []
    for i in range(len(l_top_hastags)):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("hashtags")
    plt.ylabel("nbre apparition")
    plt.tick_params(axis='x', rotation=60)
    plt.tight_layout()
    plt.show()
    
l_mention = list()
for i in range(len(l_tweets)):
    l_mention.append(l_tweets[i].find_mention())

l_mention1 = list()
for i in range(len(l_mention)):
    for j in range(len(l_mention[i])):
        l_mention1.append(l_mention[i][j])

l_mention2 = list()
a = 0
for i in l_mention1:
    
    if (i in l_mention2) == False:
        l_mention2.append(l_mention1[a])
    a += 1
l_mention_final = list()  
for i in range(len(l_mention2)):
    l_mention_final.append([l_mention1.count(l_mention2[i]),l_mention2[i]])

def top_mention(k):
    l = sorted(l_mention_final, reverse =True)
    if k > len(l):
        k = len(l)
    l_f = []
    x = []
    y = []
    for i in range(k):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("mention")
    plt.ylabel("nbre apparition")
    plt.show()
    
def nombres_mentions():
    l = sorted(l_mention_final, reverse =True)
    l_f = []
    x = []
    y = []
    for i in range(len(l_mention_final)):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("mention")
    plt.ylabel("nbre apparition")
    plt.tick_params(axis='x', rotation=60)
    plt.tight_layout()
    plt.show()
        
        
l_users = list()
l_users_all = list()
for i in range(len(l_tweets)):
    l_users_all.append(l_tweets[i].affichage_auteur())
    if l_tweets[i].affichage_auteur() in l_users:
        pass
    else:
        l_users.append(l_tweets[i].affichage_auteur())

nb_tweet_by_user = list()
for i in range(len(l_users)):
    nb_tweet_by_user.append([l_users_all.count(l_users[i]),l_users[i]])



def top_users(k):
    l = sorted(nb_tweet_by_user, reverse =True)
    if k > len(l):
        k = len(l)
    l_f = []
    x = []
    y = []
    for i in range(k):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("utilisateur")
    plt.ylabel("nombre de tweets")
    plt.show()
    
    
def nombre_publication_users():
    l = sorted(nb_tweet_by_user, reverse =True)
    l_f = []
    x = []
    y = []
    for i in range(len(nb_tweet_by_user)):
       l_f.append(l[i])
    for i in l_f:
        for j in i:
            if type(j) is type(int()):
                y.append(j)
            else:
                x.append(j)
    plt.bar(x,y,width = 0.25 , color = "blue")
    plt.xlabel("utilisateur")
    plt.ylabel("nombre de tweets")
    plt.tick_params(axis='x', rotation=60)
    plt.tight_layout()
    plt.show()

class User():
    def __init__(self, auteur, nbre, message = [] ,mentions = 0):
        self.nom = auteur
        self.nb_tweets = nbre
        self.message = message
        self.mentions = mentions
    
    def affichage_auteur(self):
        return self.nom
    
    def nb_tweets_user(self):
        return self.nb_tweets
    
    def affichage_message(self):
        return self.message
    
    def ajouter_message(self,k):
        self.message.append(k)
    
    def mentions_(self):
        return self.mentions
    

l = sorted(nb_tweet_by_user, reverse =True)
l_f = []
cpt = []
users = []
for i in range(len(l)):
    l_f.append(l[i])

for i in l_f:
    for j in i:
        if type(j) is type(int()):
            cpt.append(j)
        else:
            users.append(j)
l_users_class = list()

for i in range(len(l)):
    l_users_class.append(User(users[i],cpt[i]))
    
l_message_autor = list()
l_all_messages = list()
d = dict()
for i in range(len(data)):
    for item, val in data[i].items():
        if item == "author_id":
            auteur = val
        if item == "text":
            message = supprime_emojis(val)
    d[auteur] = list()
    l_message_autor.append([auteur,message])
    l_all_messages.append([message])
      


 
for i in range(len(l_message_autor)):
    d[l_message_autor[i][0]].append([l_message_autor[i][1]])
         
#print(d)

def mention_in_tweets(k):
    for i in range(len(l_all_messages)):
        for j in range(len(l_all_messages[i])):
            if re.search(str(k),l_all_messages[i][j]):
                print(l_all_messages[i])

def tweet_auteur(k):
    for key, val in d.items():
        if key == k:
            print(val)

# • Les utilisateurs mentionnant un hashtag spécifique  OUI
def users_mentionnant_hashtag():
    l_users_mentionnant = list()
    regex = re.compile("(#[A-Za-z][A-Za-z0-9-_]+)")
    for key,val in d.items():
         for i in range(len(val)):
             for j in range(len(val[i])):
                if re.search(regex,val[i][j]):
                    l_users_mentionnant.append(key)
    print("Les utilisateurs mentionnant un hashtag spécifique" ,set(l_users_mentionnant))
    
def users_mentionne_by_user(k):
    l_users_mentionne_by_user = list()
    regex = re.compile("(@[A-Za-z][A-Za-z0-9-_]+)")
    for key,val in d.items():
        for i in range(len(val)):
            for j in range(len(val[i])):
                c = regex.findall(val[i][j])
                if k == key:
                    l_users_mentionne_by_user.append(regex.findall(val[i][j]))
    return l_users_mentionne_by_user



def Parcourir_users():
    print("il y a",len(l_users_class),"users en tout")
    c = 0
            
    while 1:
        c = input("quel users ? ")
        while 1:
            try:
                c = int(c)
                break
            except:
                c = input("saisie non valide")
        print(l_users_class[c].affichage_auteur())
        while 1:
            n = input(" saississez un nombre: 0 = nom user, 1 = nbre de tweets, 2 = users mentionnés, 3: messages")
            while 1:
                    try:
                        n = int(n)
                        break
                    except:
                        n = input("saisie non valide : entrer 0, 1, 2, 3")
            if n == 0:
                print(l_users_class[c].affichage_auteur())
            if n == 1:
                # • Le nombre de publications par utilisateur OUI
                print(l_users_class[c].nb_tweets_user())
            if n == 2:
                print(users_mentionne_by_user(l_users_class[c].affichage_auteur()))
            if n == 3:
                # • L’ensemble de tweets d’un utilisateur spécifique OUI
                print(d[l_users_class[c].affichage_auteur()])                
            arret = input("voulez vous continuer à analyse l'utilisateur? (oui ou non) ")
            if arret == "oui":
                pass
            elif arret == "non": 
                break
            else:
                pass
        other_tweet = input("analyser un autre user ? (oui ou non) ")
        if other_tweet == "oui":
            pass
        else:
            break
        
def Start():
    a = input("Voulez vous parcourir les tweets ? ")
    if a == "oui":
        aff_tweets = input("voulez vous afficher tout les tweets ? ")
        if aff_tweets == "oui":
            for i in range(len(l_all_messages)):
                print(l_all_messages[i])
        Parcourir_tweet()
    else:
        pass
    
    b = input("Voulez vous voir un top k ou un nensemble ? ")
    if b == "oui":
        while 1:
            f = input("0 : top,  1 : ensemble ")
            while 1:
                try:
                    f = int(f)
                    break
                except:
                    f = input("saisie non valide : 0 : top,  1 : ensemble ")
            if f == 0:
                c = input(" entrer 0, 1 ou 2 (0 : top hashtags, 1 : top mentions, 2 : top users) ")
                while 1:
                    try:
                        c = int(c)
                        break
                    except:
                        c = input("saisie non valide : entrer 0, 1 ou 2")
                if c == 0:
                    # • Top K hashtags (k est un paramètre passé par l’utilisateur) OUI
                    k = input("top combien ? ")
                    while 1:
                        try:
                            k = int(k)
                            break
                        except:
                             k = input("saisie non valide")
                    top_hastag(k)
                elif c == 1:
                    # • Top K utilisateurs mentionnés OUI
                    k = input("top combien ? ")
                    while 1:
                        try:
                            k = int(k)
                            break
                        except:
                             k = input("saisie non valide")
                    top_mention(k)
                elif c==2:
                    # • Top K utilisateurs OUI
                    k = input("top combien ? ")
                    while 1:
                        try:
                            k = int(k)
                            break
                        except:
                             k = input("saisie non valide")
                    top_users(k)
                else:
                    pass
              
            if f == 1:
                c = input("0 : ensemble des hashtags, 1 : ensemble des mentions, 2 : ensemble des users) ")
                while 1:
                    try:
                        c = int(c)
                        break
                    except:
                        c = input("saisie non valide : entrer 0, 1 ou 2")
                if c == 0:
                    # • Le nombre de publications par hashtag OUI
                    nombre_publication_hashtags()
                    
                elif c == 1:
                    nombres_mentions()
                elif c==2:
                    nombre_publication_users()
                else:
                    pass
            other_top = input("other top ? ")
            if other_top == "oui":
                pass
            else:
                break
            
    w = input("voulez vous rechercher quelque chose ? ")
    if w == "oui":
        while 1:
            c = input("0 : rechercher les tweets d'un user, 1 : mention dans tweet, 2 : users_mentionnant un hashtag")
            while 1:
                    try:
                        c = int(c)
                        break
                    except:
                        c = input("saisie non valide : entrer 0, 1 ou 2")
            
            if c == 0:
                tweet_auteur(input("entrer l'identifiant"))
            if c == 1:
                # • L’ensemble de tweets mentionnant un utilisateur spécifique  OUI
                mention_in_tweets(input("entrer user"))
            if c == 2:
                # • Les utilisateurs mentionnant un hashtag spécifique  OUI
                users_mentionnant_hashtag()

                    
            other_rech = input("voulez vous continuer à faire des recherches ?")
            if other_rech == "oui":
                pass
            else:
                break         

    
    d = input("voulez vous parcourir les users ? ")
    if d == "oui":
        Parcourir_users()
    else:
        pass


lancer_app = input("Voulez vous lancer  InPoDa (analyse de tweets) ? ")
if lancer_app == "oui":
    Start()
    

# . interface OUI

# • Top K topics NON 
# • Le nombre de publications par topic NON