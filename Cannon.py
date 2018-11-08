from tkinter import *
import math

g = 9.8
root = Tk()
root.geometry('500x500')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


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
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standart_radius

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
