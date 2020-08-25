#!/usr/bin/env python

# Import modules
from turtle import *

# affichage du message d'entré
print ("**** tracer un octogone ***")

# on initialise la taille de la fenetre
setup(600, 500)

# on affiche le titre de notre fenetre
title("un octogone trace ( la tortue )")


# on initialise la couleur de l'arriere plan de notre fenetre
bgcolor('light blue')

#la couleur du tracé
color(('red'))
# l'epaisseur du tracé
width(3)

# en utilisant la boucle for : 
# on defini la largeur en pixel de notre 
longueur_cote = 50

print ("ce trace est fait avec la boucle for : ")
print ("angle = ", 360/80)
print ("nb = ", 8)

# avec la boucle for : on initialise notre point de depart i pour que sa fait 8 coté
for i in range(8):
    # on avance pour tracer 50 pixel de coté
    forward(longueur_cote)  #Côté
    # on tourne avec une angle de 360/80 pour faire 8 coté
    left(360/8)  #Angle

i = int(0)
input("Appuyez sur une touche pour tracer avec la boucle while :")

#on reinistialise notre tracer
reset()

# affichage du msg
print ("ce trace est fait avec la boucle while : ")
print ("angle = ", 360/80)
print ("nb = ", 8)

#la couleur du tracé
color(('blue'))
# l'epaisseur du tracé
width(5)

while i < 8:
    # on avance pour tracer 50 pixel de coté
    forward(longueur_cote)  #Côté
    # on tourne avec une angle de 360/80 pour faire 8 coté
    left(360/8)  #Angle
    # on incremente notre variable
    i = i + 1


# pour empecher la fermeture
mainloop()