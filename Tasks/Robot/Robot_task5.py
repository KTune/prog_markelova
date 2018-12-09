import Robot
r = Robot.rmap()
r.lm('task5')


def task():
    for _ in range(3):
        for _ in range(3):
            r.pt()
            r.dn()
            r.rt()
            r.pt()
            r.rt()
            r.up()
            r.pt()
            r.rt(2)
        r.pt()
        r.dn()
        r.rt()
        r.pt()
        r.rt()
        r.up()
        r.pt()
        r.dn(3)
        r.lt(14)


r.start(task)
