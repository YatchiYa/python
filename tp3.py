#!/usr/bin/env python

# Import modules
import math

# affichage 
print ("calcule du quotient et du resultat")
print ("")

# on saisie a et b

print (" saisie de a et b")
a = int(input("a = "))
b = int(input("b = "))

# calcule du quotient a % b
quotient = int(a % b)
# calcule du resultat a / b
resultat = int(a / b)

# affichage
print ("affichage : ")
print (a, "=", b,"*", resultat, "+", quotient)
