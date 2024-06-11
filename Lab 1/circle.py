from graphics import*
win = GraphWin("Circle", 532, 532)
# center = Point(200, 200)
# radius = 100
# circle = Circle(center, radius)
circle = Circle(Point(232, 232), 132)
circle.setOutline("red")
circle.setWidth(5)
circle.draw(win)
win.mainloop()
