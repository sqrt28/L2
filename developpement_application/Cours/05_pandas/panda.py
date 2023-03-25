import pandas as pd
import numpy as np

s = pd.Series([10,20,30,40], index=["a","b","c","d"])
print(s)
df = pd.DataFrame(columns=["s","b","c","d"], index=["chat",'singe',"souris"], data = [np.arange(10,14), np.arange(20,24),np.arange(30,34)])
print(df)
df.columns = "paris" , "lyon", "clays", "lisbonne"
dico = {"a" : np.arange(10,12), "b": np.arange(14,16)}
print(pd.DataFrame(dico))
print(df.head(2)) #deux premières lignes
print(df["paris"]) # sélctionne une colonne
print(df.loc["chat"]) #séméctionne une ligne
print(df.iloc[0]) #séléctionne la ligne 0 eTC..
print(df.loc["souris","lisbonne"])
print(df[df["lisbonne"]> 15])
datal = {"Lyon": [10,23,17], "Paris": [3,15,20]}
df2 = pd.DataFrame.from_dict(datal)
df2.index = ("chat","souris","chiens")
print(df2)
print(pd.concat((df,df2)))


#chercher le fichier
df = pd.read_csv("transferrin_report.csv")
df.head()
df = pd.read_csv("transferrin_csv", index_col ="PDB 10")
df.dtypes
df.info()
df.info(memory_usage="deep")
df.describe()
df["Source"].value_counts()
df.groupby(["Source"]).mean()

