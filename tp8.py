#!/usr/bin/env python

# Import modules
import math

# on affiche le message d'entree
print ("----- liste de points ----")
print("")

# on initialise notre liste de coordonnee
coords = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]

# affichage de notre liste
print ("notre liste de coords : ")
print (coords)
print("")

# on creer une liste ordos vide
ordos = []

for (a,b) in coords:
    # on ajoute chaque element de notre coord a notre ordo
    # sachant que : 
    # a represente le premier element du couple (a,b) = (4,5), ou (9,3) ou ...
    # b represente le deuxieme element du couple (a,b) = (4,5), ou (9,3) ou ...
    ordos.append((a,b))

# affichage 
print ("notre liste de ordos copiee : ")
print (ordos)
print("")

# on initialise la variable position pour avoir la position du tuple dans notre liste ou y est supperieur a 7
position = int(0)

for (a,b) in ordos:
    # sachant que : 
    # a represente le premier element du couple (a,b) = (4,5), ou (9,3) ou ...
    # b represente le deuxieme element du couple (a,b) = (4,5), ou (9,3) ou ...
    # on verifie chaque y si suppreieur a 7 => on borne a 7
    if (b > 7):
        # on met b = 7
        b = 7
        # et on modifie le tuple dans notre liste ordos
        ordos[position] = (a,b)
    position = position + 1

# affichage 
print ("notre liste de ordos modifiee et bornee les y par 7 : ")
print (ordos)


