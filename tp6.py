#!/usr/bin/env python

# Import modules
import math

a = int(0)
ret = int(0)
range = [1, 2, 3, 4, 5, 6]

while (a <= 0 or a > 12):
    print ("entrez un chiffre enter [1:12] please : "),
    a = int(input("a = "))

for i in range:
    for j in range:
        if (i + j) == a:
            print ("combinaison : ", i, "+", j)
            ret = ret + 1

print ("il y'a (", ret, ") facons de faire", a, "avec deux des")
print ("combinaise = ", ret)
