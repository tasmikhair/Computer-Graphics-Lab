import graphics

# Set up the graphics window
win = graphics.GraphWin("Circle", 700, 700)

# Define the center and radius of the circle
center = graphics.Point(350, 350)
radius = 232

# Initialize the x and y coordinates to draw the circle
x = 0
y = radius
d = 3 - 2 * radius

# Draw the circle using Bresenham's algorithm
while x <= y:
    # Draw the points of the circle in all eight octants
    graphics.Point(x + center.getX(), y + center.getY()).draw(win)
    graphics.Point(y + center.getX(), x + center.getY()).draw(win)
    graphics.Point(-x + center.getX(), y + center.getY()).draw(win)
    graphics.Point(-y + center.getX(), x + center.getY()).draw(win)
    graphics.Point(-x + center.getX(), -y + center.getY()).draw(win)
    graphics.Point(-y + center.getX(), -x + center.getY()).draw(win)
    graphics.Point(x + center.getX(), -y + center.getY()).draw(win)
    graphics.Point(y + center.getX(), -x + center.getY()).draw(win)

    # Update the x and y coordinates
    x += 1
    if d > 0:
        y -= 1
        d += 4 * (x - y) + 10
    else:
        d += 4 * x + 6

# Wait for a mouse click to close the window
win.getMouse()
win.close()
