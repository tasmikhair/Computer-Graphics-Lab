def drawCharacterOutline(x, y, ch, scale):
    if ch == 'A':
        drawLine(x, y, x + 10 * scale, y + 20 * scale)
        drawLine(x + 10 * scale, y + 20 * scale, x + 20 * scale, y)
        drawLine(x + 5 * scale, y + 10 * scale, x + 15 * scale, y + 10 * scale)
    # Add outlines for other characters as needed
    else:
        print("Character not supported!")
