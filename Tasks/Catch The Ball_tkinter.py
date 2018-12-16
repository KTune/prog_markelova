from tkinter import *
import random
from random import randrange as rnd

root = Tk()
root.geometry('800x800')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

COLORS = ['papaya whip', 'blanched almond', 'peach puff', 'mint cream', 'azure', 'alice blue', 'lavender blush',
          'misty rose', 'dark slate gray', 'navy', 'cornflower blue', 'medium blue', 'light sky blue', 'pale turquoise',
          'turquoise', 'cyan', 'aquamarine', 'dark green', 'dark sea green', 'sea green', 'spring green',
          'green yellow', 'lime green', 'khaki', 'light goldenrod', 'salmon', 'deep pink', 'dark orchid', 'thistle',
          'coral1', 'OrangeRed2', 'maroon1']


def new_ball():
    global xball, yball, r, ball
    canv.delete(ball)
    xball = rnd(100, 700)
    yball = rnd(100, 700)
    r = rnd(30, 70)
    ball = canv.create_oval(xball - r, yball - r, xball + r, yball + r, fill=random.choice(COLORS),
                            outline=random.choice(COLORS), width=0)


def click(event):
    global x, y
    x = event.x
    y = event.y
    if (x - xball) ** 2 + (y - yball) ** 2 <= r ** 2:
        global points
        points += 1
    else:
        if (x - xball) ** 2 + (y - yball) ** 2 > r ** 2:
            points -= 1


def tick():
    root.after(1500, tick)
    canv.delete(ALL)
    new_ball()
    canv.create_text(20, 20, text=points, font='Arial 20')


def right_click(event):  # чтобы появился новый шарик, если не найден прошлый
    canv.delete(ALL)


ball = (-1000, 0, 0, 0)
points = 0

canv.bind('<Button-1>', click)
canv.bind('<Button-3>', right_click)
root.after_idle(tick)

root.mainloop()
