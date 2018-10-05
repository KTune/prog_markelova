import graphics as gr
window = gr. GraphWin ("interest",500,500)
window.setBackground("#B3FFE5")

cloud1 = gr. Circle(gr. Point(280,80),20)
cloud1.setFill("#E6FFFF")
cloud1.setOutline("#E6FFFF")
cloud1.draw(window)

cloud2 = gr. Circle(gr. Point(308,87),20)
cloud2.setFill("#E6FFFF")
cloud2.setOutline("#E6FFFF")
cloud2.draw(window)

cloud3 = gr. Circle(gr. Point(315,110),20)
cloud3.setFill("#E6FFFF")
cloud3.setOutline("#E6FFFF")
cloud3.draw(window)

cloud4 = gr. Circle(gr. Point(340,109),20)
cloud4.setFill("#E6FFFF")
cloud4.setOutline("#E6FFFF")
cloud4.draw(window)

cloud5 = gr. Circle(gr. Point(360,100),20)
cloud5.setFill("#E6FFFF")
cloud5.setOutline("#E6FFFF")
cloud5.draw(window)


sun = gr. Circle(gr. Point(120,100),60)
sun.setFill("#FFD500")
sun.setOutline("#FFD500")
sun.draw(window)


txt = gr. Text(gr. Point(250,250), "Whatcha doing?")
txt.setSize(20)
txt.setTextColor("#550066")
txt.draw(window)

hill = gr. Circle(gr. Point(550,550),300)
hill.setFill("#99E600")
hill.setOutline("#99E600")
hill.draw(window)

grass = gr. Circle(gr. Point(250,1100),750)
grass.setFill("#008000")
grass.setOutline("#008000")
grass.draw(window)




window.getMouse()
window.close()
