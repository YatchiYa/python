#!/usr/bin/env python

# Import modules
import math

# ---------------------------------------------------------------------------------------------
# on initialise le compteur de notre boucle while
i = int(1)

# on initilialise la valeur du retour de la somme
somme = int(0)

print ("affichage des 10 premier entier en utilisant la boucle while")
# un retour a la ligne ene plus
print ("")

while i <= 10:
    # on ajoute a chaque fois + i qui va etre (1 apres 2 apres 3 apres 4 apres ...)
    somme = somme + i
    # on incremente notre variable i
    i = i + 1

#affichage
print ("la somme = [", somme, "]")
# un retour a la ligne ene plus
# un retour a la ligne ene plus
print ("")
# ---------------------------------------------------------------------------------------------

print ("affichage des 10 premier entier en utilisant la methode simple")
# un retour a la ligne ene plus
# un retour a la ligne ene plus
print ("")

# on initialise la valeur du n = 10
n = int(10)
somme = 0

#on calcule la somme
somme = n*(n + 1)/(2)

#affichage
print ("la somme = [", int(somme), "]")
# un retour a la ligne ene plus
print ("")
# ---------------------------------------------------------------------------------------------

print ("affichage des 10 premier entier en utilisant la boucle for")
# un retour a la ligne ene plus
print ("")

somme = 0
#appel de la boucle for pour chaque i
for j in range(11):
    # on ajoute a chaque fois + i qui va etre (1 apres 2 apres 3 apres 4 apres ...)
    somme = somme + j

# affichage
print ("la somme = [", int(somme), "]")
# un retour a la ligne ene plus