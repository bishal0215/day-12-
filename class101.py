import turtle 
import random
t=turtle.Turtle()
t.speed(0)
colors=["red","blue","green","yellow","purple","green"]

for i in range(360):
    t.color(random.choice(colors))
    t.forward(random.randint(20,150))
    t.right(random.randint(0,360))
   

t.hideturtle()
turtle.done()
