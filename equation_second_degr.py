#!/usr/bin/python

# Hello world python program

import math

# a*x**2 + b*x + c un trinome du second degre.
print "Soit une equation de la forme : ax^2 + bx + c = 0"

# On rentre les valeurs de a, b et c.
# On souhaite que a, b et c soient des nombres reels (float en anglais)
# et non une chaine de charactere (comme pour une phrase)

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Calcul du discriminant delta = b**2 - 4*a*c.
# Remarques : 4*a*c =/= 4ac qui est un autre nom de variable
delta = b**2 - 4*a*c

# Si delta est negatif
if(delta < 0):
    print("L'equation n'a pas de solution")

# Sinon, delta peut etre positif ou nul    
else:
    # Si delta est nul
    if (delta == 0):
        print("L'equation a une solution double.")
        x = -b / (2.*a)
        print ("La solution est x = ",x)
    
    #Sinon,  delta ne peut plus qu'etre positif.
    else:
        print("L'equation a deux solutions solutions.")
        x1 = (-b - math.sqrt(delta)) /(2*a)
        x2 = (-b + math.sqrt(delta)) /(2*a)
        print ("Les solutions sont x1 = ", x1, " et ", x2)