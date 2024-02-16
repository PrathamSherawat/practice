import turtle
t=turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
for i in range(240):
    t.color("pink")
    t.circle(i)
    t.right(5)

turtle.done()