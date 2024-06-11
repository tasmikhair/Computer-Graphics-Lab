import graphics

# Set up the graphics window
win = graphics.GraphWin("Circle", 800, 800)

# Define the center and radius of the circle
center = graphics.Point(350, 350)
radius = 232

# Initialize the x and y coordinates to draw the circle
x = 0
y = radius
p = 1 - radius

# Draw the circle using Midpoint algorithm
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

    # Update the x and y coordinates based on the Midpoint algorithm
    x += 1
    if p < 0:
        p += 2 * x + 1
    else:
        y -= 1
        p += 2 * (x - y) + 1

# Wait for a mouse click to close the window
win.getMouse()
win.close()
