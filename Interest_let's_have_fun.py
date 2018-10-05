import graphics as gr
window = gr. GraphWin("interest", 500, 500)
window.setBackground("#B3FFE5")


def draw_cloud(x, y):
    cloud_color = "#E6FFFF"
    circle_centers = [(x-20, y-20), (x+8, y-13), (x+15, y+10),
                      (x+40, y+9), (x+60, y)]
    for x, y in circle_centers:
        circle = gr.Circle(gr.Point(x, y), 20)
        circle.setFill(cloud_color)
        circle.setOutline(cloud_color)
        circle.draw(window)


def draw_sun():
    sun = gr. Circle(gr. Point(120, 100), 60)
    sun.setFill("#FFD500")
    sun.setOutline("#FFD500")
    sun.draw(window)


def draw_txt():
    txt = gr. Text(gr. Point(250, 250), "Whatcha doing?")
    txt.setSize(20)
    txt.setTextColor("#550066")
    txt.draw(window)


def draw_hill():
    hill = gr. Circle(gr. Point(550, 550), 300)
    hill.setFill("#99E600")
    hill.setOutline("#99E600")
    hill.draw(window)


def draw_grass():
    grass = gr.Circle(gr.Point(250, 1100), 750)
    grass.setFill("#008000")
    grass.setOutline("#008000")
    grass.draw(window)


def draw_answerbox():
    input_box = gr.Entry(gr.Point(250, 280), 10)
    input_box.setFill("#FFFFFF")
    input_box.draw(window)


for x, y in [(240,100), (300,180), (380,100)]:
    draw_cloud(x,y)
draw_hill()
draw_grass()
draw_sun()
draw_txt()
draw_answerbox()

window.getMouse()
window.close()
