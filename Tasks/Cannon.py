from random import randrange as rnd, choice
import math
from tkinter import *
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)


class Cannon:

    def __init__(self):
        self.f_power = 10
        self.f_on = 0
        self.direction = math.pi / 4
        self.x = x_start
        self.y = y_start
        self.line_length = 100
        self.id = canv.create_line(self.x, self.y, self.x + self.line_length, self.y, width=30, fill="black")

    def fire_start(self, event):
        self.f_on = 1

    def fire_end(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Shell()
        new_ball.r += 5
        self.direction = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.Vx = self.f_power * math.cos(self.direction)
        new_ball.Vy = -self.f_power * math.sin(self.direction)
        balls += [new_ball]
        self.f_on = 0
        self.f_power = 10

    def aiming(self, event=0):
        if event:
            self.direction = math.atan((event.y - self.y) / (event.x - self.x))
        if self.f_on:
            canv.itemconfig(self.id, fill='red')
        else:
            canv.itemconfig(self.id, fill='blue')
        canv.coords(self.id, x_start, y_start, x_start + max(self.f_power, 20) * math.cos(self.direction),
                    y_start + max(self.f_power, 20) * math.sin(self.direction))

    def fire_power(self):
        if self.f_on:
            if self.f_power < 100:
                self.f_power += 1
            canv.itemconfig(self.id, fill='red')
        else:
            canv.itemconfig(self.id, fill='blue')


x_start = 20
y_start = 450
standard_radius = 15


class Shell:
    def __init__(self, x=x_start, y=y_start):
        self.x, self.y = x, y
        self.Vx, self.Vy = 0, 0
        self.r = standard_radius
        self.color = choice(['blue', 'green', 'red'])
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 360

    def move(self):
        if self.y <= 500:
            self.Vy -= 1.2
            self.y -= self.Vy
            self.x += self.Vx
            self.Vx *= 0.99
            self.draw()
        else:
            if self.Vx ** 2 + self.Vy ** 2 > 10:
                self.Vy = -self.Vy / 2
                self.Vx = self.Vx / 2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.id)
            else:
                self.live -= 1
        if self.x > 780:
            self.Vx = - self.Vx / 2
            self.x = 779

    def draw(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def detect_collision(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False


class Target:
    def new_target(self):
        x = self.x = rnd(450, 780)
        y = self.y = rnd(200, 520)
        r = self.r = rnd(8, 50)
        color = self.color = 'magenta'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='20')
        self.new_target()
        self.live = 1
        self.x, self.y = 0, 0
        self.color = 'red'
        self.r = 15

    def collide(self, points=1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


target = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
cannon = Cannon()
bullet = 0
balls = []


def new_game():
    global target, screen1, balls, bullet
    target.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', cannon.fire_start)
    canv.bind('<ButtonRelease-1>', cannon.fire_end)
    canv.bind('<Motion>', cannon.aiming)

    target.live = 1
    while target.live or balls:
        for ball in balls:
            ball.move()
            if ball.detect_collision(target) and target.live:
                target.live = 0
                target.collide()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Цель уничтожена за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        cannon.aiming()
        cannon.fire_power()
    canv.itemconfig(screen1, text='')
    root.after(750, new_game)


new_game()

mainloop()
