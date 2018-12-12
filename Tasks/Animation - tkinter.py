import graphics as gr
import time
window = gr. GraphWin("interest", 500, 500)
window.setBackground("#B3FFE5")


def main():
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
        global sun
        sun = gr. Circle(gr. Point(120, 100), 60)
        sun.setFill("#FFD500")
        sun.setOutline("#FFD500")
        sun.draw(window)

    def draw_txt():
        global txt
        txt = gr. Text(gr. Point(250, 250), "What are you doing?")
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
        answerbox = gr.Entry(gr.Point(250, 280), 10)
        answerbox.setFill("#FFFFFF")
        answerbox.draw(window)

    def draw_house():
        m = 350
        n = 420
        walls = gr.Rectangle(gr.Point(m, m), gr.Point(n, n))
        walls.setFill("#CC2200")
        walls.setOutline("#CC2200")
        roof = gr.Polygon(gr.Point(m, m), gr.Point(m+35, n-120), gr.Point(m+70, m))
        roof.setFill("#FF7E00")
        roof.setOutline("#FF7E00")
        roof.draw(window)
        walls.draw(window)

    for x, y in [(240, 100), (300, 180), (380, 100)]:
        draw_cloud(x, y)

    def draw_birds(x, y):
        global bird1_l, bird1_r, bird2_l, bird2_r, bird3_l, bird3_r
        bird1_r = gr.Line(gr.Point(x, y), gr.Point(x + 20, y - 5))
        bird1_l = gr.Line(gr.Point(x + 20, y - 5), gr.Point(x + 10, y + 10))
        bird1_r.draw(window)
        bird1_l.draw(window)

        bird2_r = gr.Line(gr.Point(x + 50, y + 25), gr.Point(x + 70, y + 20))
        bird2_l = gr.Line(gr.Point(x + 70, y + 20), gr.Point(x + 60, y + 35))
        bird2_r.draw(window)
        bird2_l.draw(window)

        bird3_r = gr.Line(gr.Point(x + 85, y - 10), gr.Point(x + 105, y - 15))
        bird3_l = gr.Line(gr.Point(x + 105, y - 15), gr.Point(x + 100, y))
        bird3_r.draw(window)
        bird3_l.draw(window)

    for x, y in [(240, 100)]:
        draw_birds(x, y)

    draw_hill()
    draw_grass()
    draw_sun()
    draw_txt()
    draw_answerbox()
    draw_house()

    def animation():
        for _ in range(20):
            bird1_r.move(1, -1)
            bird1_l.move(1, -1)
            bird2_l.move(1, -1)
            bird2_r.move(1, -1)
            bird3_l.move(1, -1)
            bird3_r.move(1, -1)

            sun.move(-1, 0)

            txt.move(0, -1)

            time.sleep(0.2)

    animation()

    window.getMouse()
    window.close()


main()
