from tkinter import *
from random import randrange as rnd, choice
import math
import time

g = 9.8
root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

def draw_cannon():
    canv.create_line(70, 550, 160, 480, width=30, fill="black")
    canv.create_oval(0, 600, 100, 500,outline="black", fill="black")


class Cannon:
    max_velocity = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shell_num = None
        self.direction = math.pi / 4

    def aim(self, x, y):

        pass

    def fire(self, dt):

        pass


class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        canv.create_oval(x1, y1, x2, y2, fill='orange', outline="pink")

    def go(self, dt):
        ax, ay = 0, g
        self.x += self.Vx*dt + ax*(dt**2)/2
        self.y += self.Vy*dt + ay*(dt**2)/2
        self.Vx += ax*dt
        self.Vy += ay*dt

    def detect_collision(self, other):
        length = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return length <= self.r + other.r


class Target:
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_raduis

    def go(self, dt):
        ax, ay = 0, g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += ay * dt

    def collide(self, other):
        pass  # TODO



shell2 = Shell(80, 98, 86, 86)

draw_cannon()
root.mainloop()
