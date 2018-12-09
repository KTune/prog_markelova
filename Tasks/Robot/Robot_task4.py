import Robot
r = Robot.rmap()
r.lm('task4')


def task():
    while r.fl():
        r.lt()
    while r.fd():
        r.dn()
    for y in range(3):
        for x in range(5):
            r.rt()
            r.up()
            r.pt()
        r.lt(5)
        r.dn(3)


r.start(task)
