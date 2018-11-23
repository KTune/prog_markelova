import graphics as gr
window = gr. GraphWin("interest", 500, 500)
window.setBackground("#B3FFE5")


def draw_cloud1():
    cloud1 = gr. Circle(gr. Point(280, 80), 20)
    cloud1.setFill("#E6FFFF")
    cloud1.setOutline("#E6FFFF")
    cloud1.draw(window)


def draw_cloud2():
    cloud2 = gr. Circle(gr. Point(308, 87), 20)
    cloud2.setFill("#E6FFFF")
    cloud2.setOutline("#E6FFFF")
    cloud2.draw(window)


def draw_cloud3():
    cloud3 = gr. Circle(gr. Point(315, 110), 20)
    cloud3.setFill("#E6FFFF")
    cloud3.setOutline("#E6FFFF")
    cloud3.draw(window)


def draw_cloud4():
    cloud4 = gr. Circle(gr. Point(340, 109), 20)
    cloud4.setFill("#E6FFFF")
    cloud4.setOutline("#E6FFFF")
    cloud4.draw(window)


def draw_cloud5():
    cloud5 = gr. Circle(gr. Point(360, 100), 20)
    cloud5.setFill("#E6FFFF")
    cloud5.setOutline("#E6FFFF")
    cloud5.draw(window)



def draw_cloud6():
        cloud1 = gr.Circle(gr.Point(380, 140), 20)
        cloud1.setFill("#E6FFFF")
        cloud1.setOutline("#E6FFFF")
        cloud1.draw(window)


def draw_cloud7():
        cloud2 = gr.Circle(gr.Point(408, 147), 20)
        cloud2.setFill("#E6FFFF")
        cloud2.setOutline("#E6FFFF")
        cloud2.draw(window)


def draw_cloud8():
        cloud3 = gr.Circle(gr.Point(415, 170), 20)
        cloud3.setFill("#E6FFFF")
        cloud3.setOutline("#E6FFFF")
        cloud3.draw(window)


def draw_cloud9():
        cloud4 = gr.Circle(gr.Point(440, 169), 20)
        cloud4.setFill("#E6FFFF")
        cloud4.setOutline("#E6FFFF")
        cloud4.draw(window)

def draw_cloud10():
        cloud5 = gr.Circle(gr.Point(460, 160), 20)
        cloud5.setFill("#E6FFFF")
        cloud5.setOutline("#E6FFFF")
        cloud5.draw(window)


def draw_sun():
    sun = gr. Circle(gr. Point(120, 100), 60)
    sun.setFill("#FFD500")
    sun.setOutline("#FFD500")
    sun.draw(window)


def draw_txt():
    txt = gr. Text(gr. Point(250, 450), "Whatcha doing?")
    txt.setSize(20)
    txt.setTextColor("#550066")
    txt.draw(window)


def draw_hill():
    hill = gr. Circle(gr. Point(550, 550), 300)
    hill.setFill("#99E600")
    hill.setOutline("#99E600")
    hill.draw(window)


def draw_grass():
    grass = gr. Circle(gr. Point(250, 1100), 750)
    grass.setFill("#008000")
    grass.setOutline("#008000")
    grass.draw(window)


draw_cloud1()
draw_cloud2()
draw_cloud3()
draw_cloud4()
draw_cloud5()
draw_cloud6()
draw_cloud7()
draw_cloud8()
draw_cloud9()
draw_cloud10()
draw_hill()
draw_grass()
draw_sun()
draw_txt()

window.getMouse()
window.close()
