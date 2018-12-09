import Robot
r = Robot.rmap()
r.lm('task2')


def task():
    for x in range(7):
        r.up()
        r.pt()
        r.up()
        r.rt()
        r.pt()
        r.dn()
        r.dn()
        r.pt()
        r.rt()
    r.up()
    r.pt()


r.start(task)
