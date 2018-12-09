import Robot
r = Robot.rmap()
r.lm('task3')


def task():
    while not r.wr():
        if not r.wd() and r.wu():
            r.dn()
            r.up()
        r.rt()


r.start(task)
