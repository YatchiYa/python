
from turtle import *

print ("tracer un octogone ")

setup(600, 500)
title("un octogone trace ( la tortue )")
bgcolor('light blue')
dot(10, 'black')
up()
goto(0, -50)
down()
color(('red'))
width(3)
circle(50, steps=8)

# pour empecher la fermeture
mainloop()