#!/usr/bin/env python

# Import modules
import math

#on declare la variable a initial
a = int(0)
#on declare la variable i comme compteur de la boucle while 
i = int(1)

# affichage simple
print ("les multiple de 7 avec etoile (*) sur les multiple de 3")

# pour mettre un espace entre les deux bloc ; 2 retour a la ligne juste pour l'affichage
print ("")

# on entre dans la boucle why
while (i <= 20):
    # la valeur du retour qu"on incremente a chaque fois
    a = 7 * i
    #l'affichage de la valeur
    # end =' ' c'est pour eviter le retour a la ligne
    print (a, end='')
    # on regarde si la valeur est un multiple de 3 donc le modulo de a sur 3 sera 0
    quotien = a % 3
    # si la valeur est 0 on met une etoile a coté sinon on met rien
    if (quotien == 0):
        print ("*", end=' ')
    else:
        print (" ", end='')
    # on incremente notre i 
    i = i + 1