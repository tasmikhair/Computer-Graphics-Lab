from graphics import *

# Define window coordinates
xmin, xmax, ymin, ymax = 100, 400, 100, 300

# Define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Function to compute region code for a point (x, y)
def computeCode(x, y):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Function to clip a polygon against a rectangular window
def sutherlandHodgmanClip(polygon):
    clipped_polygon = []

    # Clip against left edge
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)

        if code2 & LEFT:
            if not code1 & LEFT:
                clipped_polygon.append((xmin, y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)))
        else:
            clipped_polygon.append((x2, y2))
        if not code2 & LEFT:
            clipped_polygon.append((x2, y2))

    # Clip against right edge
    polygon = clipped_polygon.copy()
    clipped_polygon.clear()
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)

        if code2 & RIGHT:
            if not code1 & RIGHT:
                clipped_polygon.append((xmax, y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)))
        else:
            clipped_polygon.append((x2, y2))
        if not code2 & RIGHT:
            clipped_polygon.append((x2, y2))

    # Clip against bottom edge
    polygon = clipped_polygon.copy()
    clipped_polygon.clear()
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)

        if code2 & BOTTOM:
            if not code1 & BOTTOM:
                clipped_polygon.append((x1 + (x2 - x1) * (ymin - y1) / (y2 - y1), ymin))
        else:
            clipped_polygon.append((x2, y2))
        if not code2 & BOTTOM:
            clipped_polygon.append((x2, y2))

    # Clip against top edge
    polygon = clipped_polygon.copy()
    clipped_polygon.clear()
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        code1 = computeCode(x1, y1)
        code2 = computeCode(x2, y2)

        if code2 & TOP:
            if not code1 & TOP:
                clipped_polygon.append((x1 + (x2 - x1) * (ymax - y1) / (y2 - y1), ymax))
        else:
            clipped_polygon.append((x2, y2))
        if not code2 & TOP:
            clipped_polygon.append((x2, y2))

    return clipped_polygon

# Main function to draw the window and perform polygon clipping
def main():
    win = GraphWin("Sutherland-Hodgman Polygon Clipping", 500, 400)
    win.setCoords(0, 0, 500, 400)

    # Draw the window
    rect = Rectangle(Point(xmin, ymin), Point(xmax, ymax))
    rect.setWidth(2)
    rect.draw(win)

    # Input polygon coordinates
    print("Enter number of vertices for polygon:")
    n = int(input())
    polygon = []
    print("Enter polygon coordinates (x, y) in clockwise or anticlockwise order:")
    for _ in range(n):
        x, y = map(int, input().split())
        polygon.append((x, y))

    # Draw the input polygon
    input_polygon = Polygon(*[Point(p[0], p[1]) for p in polygon])
    input_polygon.setWidth(2)
    input_polygon.setFill("blue")
    input_polygon.draw(win)

    # Clip the polygon
    clipped_polygon = sutherlandHodgmanClip(polygon)

    # Draw the clipped polygon
    if clipped_polygon:
        clipped_polygon_shape = Polygon(*[Point(p[0], p[1]) for p in clipped_polygon])
        clipped_polygon_shape.setWidth(2)
        clipped_polygon_shape.setFill("red")
        clipped_polygon_shape.draw(win)
        print("The clipped polygon is drawn in red.")
    else:
        print("The polygon is fully outside the window.")

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
