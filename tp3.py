#!/usr/bin/env python

# Import modules
import math

# affichage 
print "calcule du quotient et du resultat"

# on saisie a et b
a = int(input("a = "))
b = int(input("b = "))

# calcule du quotient a % b
quotient = a % b
# calcule du resultat a / b
resultat = a / b

# affichage
print ("affichage : ")
print a, "=", b,"*",resultat, "+", quotient
