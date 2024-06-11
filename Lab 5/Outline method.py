import turtle

# Function to draw a line between two points (x1, y1) and (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Function to draw a character using outline method
def drawCharacterOutline(x, y, ch, scale):
    if ch == 'A':
        drawLine(x, y, x + 10 * scale, y + 20 * scale)
        drawLine(x + 10 * scale, y + 20 * scale, x + 20 * scale, y)
        drawLine(x + 5 * scale, y + 10 * scale, x + 15 * scale, y + 10 * scale)
    # Add outlines for other characters as needed
    else:
        print("Character not supported!")

def main():
    # Setup the turtle screen
    turtle.setup(width=600, height=600)
    turtle.speed(0)  # Set maximum speed

    # Example: drawing character 'A' at position (100, 100) with a scale factor of 3
    drawCharacterOutline(100, 100, 'A', 3)

    # Hide turtle
    turtle.hideturtle()

    # Keep the window open until closed by the user
    turtle.done()

if __name__ == "__main__":
    main()
