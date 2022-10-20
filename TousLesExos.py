# Exercice 1

# Variable "prenom" qui contient Pierre
from operator import truediv

prenom = "Pierre"
print(prenom)

# Variable "age" qui contient 20
age = 20
print(age)

# Variable "majeur" qui contient booleen Vrai
majeur = True
print(majeur)

# Variable "compte_en_banque" qui contient nombre décimal 20135,384
compte_en_banque = float(20135.384)
print(compte_en_banque)

# Variable "amis" qui contient liste de trois chaîne Marie, Julien et Adrien
amis = ["Marie", "Julien", "Adrien"]
print(amis)

# Variable "parents" qui contient un tuple avec 2 chaînes de caractères Marc et Caroline
parents = ("Marc", "Caroline")
print(parents)


# Exercice 2

# Correction de l'erreur :
# Erreur dans la variable site_web, corrigez la :
site_web = "Voila"
print(site_web)


# Exercice 3

# code a corriger pour le 003
# nombre = 15
# print("Le nombre est " + nombre)

nombre = 15
nombreRefactor = int(nombre)
print(f"Le nombre est  {nombreRefactor}")


# Exercice 4 (Inutile)

# Exercice 5

# le 004 trop facile voici le 005 :

# Dans cet exercice, nous allons utiliser les nouvelles fonctionnalités de Python 3, afin de printer les 3 variables a, b et c,
# séparées par un symbole d'addition (+).
# Votre script doit donc afficher : 2 + 6 + 3.
# a = 2
# b = 6
# c = 3

a, b, c = [2, 6, 3]
print(a, b, c, sep=" + ")


# Exercice 6

list1 = range(3)
list2 = range(5)

print(list(list2))


# Exercice 7

typeInteger = int
typeChar = str

typeInteger = 1
typeChar = 2


prenom = "Pierre"
if isinstance(prenom, str):
    print("La variable est une chaîne de caractère")
else:
    print("La variable n'est pas une chaîne de caractère")
 

# Exercice 8

phrase = "Bonjour les amis"
nouvelle_phrase = phrase.replace("Bonjour", "Salut")
print(nouvelle_phrase)


