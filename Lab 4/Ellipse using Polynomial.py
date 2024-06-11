import pygame
import sys
import math

def drawEllipse(a, b, center_x, center_y):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Ellipse Drawing')

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # White background

        # Ax^2 + By^2 + Cx + Dy + E = 0
        pygame.draw.ellipse(screen, (255, 0, 0), (center_x - a, center_y - b, 2 * a, 2 * b), 1)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

# Call the drawEllipse function with your desired parameters
center_x = 400  # X-coordinate of the center
center_y = 300  # Y-coordinate of the center
a = 150  # Horizontal radius
b = 100  # Vertical radius
drawEllipse(a, b, center_x, center_y)