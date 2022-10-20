# # Exercice 1

# Affecter des elements à des variables

# # Variable "prenom" qui contient Pierre
# from operator import truediv

# prenom = "Pierre"
# print(prenom)

# # Variable "age" qui contient 20
# age = 20
# print(age)

# # Variable "majeur" qui contient booleen Vrai
# majeur = True
# print(majeur)

# # Variable "compte_en_banque" qui contient nombre décimal 20135,384
# compte_en_banque = float(20135.384)
# print(compte_en_banque)

# # Variable "amis" qui contient liste de trois chaîne Marie, Julien et Adrien
# amis = ["Marie", "Julien", "Adrien"]
# print(amis)

# # Variable "parents" qui contient un tuple avec 2 chaînes de caractères Marc et Caroline
# parents = ("Marc", "Caroline")
# print(parents)


# # Exercice 2

# Correction de la variable site_web

# # Correction de l'erreur :
# # Erreur dans la variable site_web, corrigez la :
# site_web = "Voila"
# print(site_web)


# # Exercice 3

# # code a corriger pour le 003
# # nombre = 15
# # print("Le nombre est " + nombre)

# Correction du code

# nombre = 15
# nombreRefactor = int(nombre)
# print(f"Le nombre est  {nombreRefactor}")


# # Exercice 4 (Inutile)

# # Exercice 5

# # le 004 trop facile voici le 005 :

# # Dans cet exercice, nous allons utiliser les nouvelles fonctionnalités de Python 3, afin de printer les 3 variables a, b et c,
# # séparées par un symbole d'addition (+).
# # Votre script doit donc afficher : 2 + 6 + 3.
# # a = 2
# # b = 6
# # c = 3

# Afficher 2, 6, 3

# a, b, c = [2, 6, 3]
# print(a, b, c, sep=" + ")


# # Exercice 6
# Ca convertie l'objet range en liste

# list1 = range(3)
# list2 = range(5)

# print(list(list2))


# # Exercice 7
# Voir si la variable est bien en String

# typeInteger = int
# typeChar = str

# typeInteger = 1
# typeChar = 2


# prenom = "Pierre"
# if isinstance(prenom, str):
#     print("La variable est une chaîne de caractère")
# else:
#     print("La variable n'est pas une chaîne de caractère")
 

# # Exercice 8

# Remplacer une chaîne de caractère par une autre

# phrase = "Bonjour les amis"
# nouvelle_phrase = phrase.replace("Bonjour", "Salut")
# print(nouvelle_phrase)

# liste1 = ["pomme", "poire", "cerise", "ananas" , "banane", "qoing"]

# for x in liste1:
#     print(x)

# x = 0
# while x < len(liste1):
#     print(liste1[x])
#     x = x + 1

# liste1.sort()
# print(liste1)

# chaine = "pomme, abricot, cerise, fraise, orange"
# chaine_liste = chaine.split(", ")
# chaine_liste.sort()
# chaine_en_ordre = ", ".join(chaine_liste)
# print(chaine_en_ordre)

# import math
# rayon = int(input("Renseignez le rayon de votre sphère : " ))
# volume = (4.0*math.pi/3.0)*(rayon**3)
# print(volume)

# liste5 = [i for i in range(10, 101)]
# print(liste5)

# liste6 = [i for i in range(201) if i % 2 == 0]
# print(liste6)

# import random
# dés = random.randint(1, 6)
# print (dés)

# EXERCICE 9
# Compter le nombre d'occurences d'une lettre dans une chaîne

# lettre_a_chercher = "a"
# phrase = "Voila les amis, Alors ça va ?"
# compteur = 0
# for lettre in phrase:
#     if lettre == lettre_a_chercher:
#         compteur = compteur + 1
# print(compteur)


# Essai mais ne fonctionne pas

# phrase = "Voila les amis, Alors ça vaeaaaaaaaaaaaa ?"
# dictionaire = {}
# compteur = 0
# for lettre in phrase:
#     if lettre == lettre:
#         list[lettre]
#         compteur = compteur + 0
#     else:
#         compte = compteur + 1
# print(lettre)