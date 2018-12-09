import turtle
wn = turtle.Screen()
andy = turtle.Turtle()
andy.shape('turtle')
for aColor in ["yellow","red","purple", "blue"]:
    andy.color(aColor)
    andy.forward(100)
    andy.left(90)

wn.exitonclick()
