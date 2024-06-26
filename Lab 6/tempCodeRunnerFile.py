from graphics import *

def main():
    win = GraphWin("My Window +_+", 500, 500)
    win.setBackground('black')
    center = Point(250, 250)
    cir = Circle(center, 70)
    cir.setFill('red')
    cir.draw(win)
    #middle line
    p1 = Point(250, 150)
    p2 = Point(250, 350)
    line = Line(p1, p2)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #left line
    p3 = Point(150, 150)
    p4 = Point(150, 350)
    line = Line(p3, p4)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #right line
    p5 = Point(350, 150)
    p6 = Point(350, 350)
    line = Line(p5, p6)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #bottom line
    p7 = Point(50, 350)
    p8 = Point(450, 350)
    line = Line(p7, p8)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #upper left line
    p9 = Point(150, 150)
    p10 = Point(240, 50)
    line = Line(p9, p10)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #upper middle line
    p11 = Point(250, 150)
    p12 = Point(340, 50)
    line = Line(p11, p12)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #upper right line
    p11 = Point(350, 150)
    p12 = Point(440, 50)
    line = Line(p11, p12)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    #top line
    p13 = Point(240, 50)
    p14 = Point(440, 50)
    line = Line(p13, p14)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    win.getMouse()
    win.close()
    
main()