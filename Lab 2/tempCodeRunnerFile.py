from graphics import *

def main():
    # Get user input for start and end points
    x1 = int(input("Enter Start- X1: "))
    y1 = int(input("Enter Start- Y1: "))
    x2 = int(input("Enter End- X2: "))
    y2 = int(input("Enter End- Y2: "))

    win = GraphWin("Faiaz's Line", 1000, 1000)

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        step = abs(dx)
    else:
        step = abs(dy)

    x_incr = dx / step
    y_incr = dy / step
    x = x1
    y = y1

    for nx in range(0, step):
        aPoint = Point(x, y)
        aPoint.draw(win)
        x = x + x_incr
        y = y + y_incr

    win.getMouse()  # pause for click in window
    win.close()

if __name__ == "__main__":
    main()



