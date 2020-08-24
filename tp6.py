#!/usr/bin/env python

# Import modules
import math

# on initialise notre variable a du input 
a = int(0)

# on initialise notre variable ret du retour du nombre de combinaison possible
ret = int(0)

# on initialise les faces du dés qu'on a disposition
range = [1, 2, 3, 4, 5, 6]

# une boucle while qui dis a l'utilisateur tant que le chiffre entré n'est pas entre 1 et 12 que ce n'est pas possible
while (a <= 0 or a > 12):
    # on entre notre variable : notre chiffre
    print ("entrez un chiffre enter [1:12] please : "),
    a = int(input("a = "))
    # si le chiffre est erreur on affiche le msg d'erreur
    if (a <= 0 or a > 12):
        print ("le chiffre que vous avez entre est impossible a realise avec deux des")
    

# on calcule le nombre de combinaison possible

# on comparge i a la liste de j 
# par exemple on commence i = 1 et (j=1 ou j=2 ou j=3 ou j=4 ou j=5 ou j=6)
#  si i+j = a (notre chiffre) on ret + 1 pour incrementer notre nombre de combinaise
# apres on fait pareil pour i=2 et (j=1 ou j=2 ou j=3 ou j=4 ou j=5 ou j=6)
# apres i=3 et (j=1 ou j=2 ou j=3 ou j=4 ou j=5 ou j=6)
# jusqu'a i=6


# donc on commence par i dans range = [1, 2, 3, 4, 5, 6] ( pour chaque valeur)
for i in range:
    # et pour chaque j dans range = [1, 2, 3, 4, 5, 6] ( pour chaque valeur)
    for j in range:
        # si i + j est egal a notre chiffre
        if (i + j) == a:
            # on affiche la combinaison et on incremente la valeur du retour
            print ("combinaison : ", i, "+", j)
            ret = ret + 1


# l'affichage final
# un retour a la ligne ene plus
print ("")
print ("il y'a (", ret, ") facons de faire", a, "avec deux des")
print ("combinaison possible = ", ret)
