import turtle
screen=turtle.Screen()
screen.bgcolor("black")
t=turtle.Turtle()
t.speed(0)
t.width(2)
colors=["red","orange","yellow","green","cyan","blue","purple"]
for i in range(360):
    t.color(colors[i%7])
    t.forward(i*2)
    t.left(59)
    for j in range(6):
        t.circle(20)
        t.left(60)

turtle.done()
