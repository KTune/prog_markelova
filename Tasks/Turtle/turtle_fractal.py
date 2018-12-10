import turtle
wn = turtle.Screen()

turtle.shape('turtle')
turtle.speed('fastest')


def figure(l, m):
    if m == 0:
        turtle.forward(l)
        return

    x = l / 4
    figure(x, m - 1)
    turtle.left(60)
    figure(x, m - 1)
    turtle.right(120)
    figure(x, m - 1)
    turtle.left(60)
    figure(x, m - 1)


def draw(l, m):
    figure(l, m)
    turtle.right(120)
    figure(l, m)
    turtle.right(120)
    figure(l, m)
    turtle.right(120)


draw(250, 4)
wn.exitonclick()
