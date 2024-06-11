from graphics import *  # Importing all classes and functions from the 'graphics' module

def main():
    win = GraphWin("My Window +_+", 500, 500)
    win.setBackground('black')
    
    center = Point(250, 250)  # center of window
    cir = Circle(center, 70)  # circle with center at (250, 250) and radius 70
    cir.setFill('red')  
    cir.draw(win)
    
    # Middle line
    p1 = Point(250, 150)
    p2 = Point(250, 350)
    line = Line(p1, p2)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Left line
    p3 = Point(150, 150)
    p4 = Point(150, 350)
    line = Line(p3, p4)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Right line
    p5 = Point(350, 150)
    p6 = Point(350, 350)
    line = Line(p5, p6)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Bottom line
    p7 = Point(50, 350)
    p8 = Point(450, 350)
    line = Line(p7, p8)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Upper left line
    p9 = Point(150, 150)
    p10 = Point(240, 50)
    line = Line(p9, p10)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Upper middle line
    p11 = Point(250, 150)
    p12 = Point(340, 50)
    line = Line(p11, p12)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Upper right line
    p13 = Point(350, 150)
    p14 = Point(440, 50)
    line = Line(p13, p14)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    # Top line
    p15 = Point(240, 50)
    p16 = Point(440, 50)
    line = Line(p15, p16)
    line.setFill('white')
    line.setWidth(2)
    line.draw(win)
    
    win.getMouse()
    win.close()

main()
