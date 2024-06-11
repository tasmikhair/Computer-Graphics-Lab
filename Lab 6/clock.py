import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")

# Define clock parameters
clock_radius = 200
center_x, center_y = WIDTH // 2, HEIGHT // 2
hour_length = 100
minute_length = 150
second_length = 180

# Define clock font
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw clock face
    pygame.draw.circle(screen, BLACK, (center_x, center_y), clock_radius, 2)

    # Draw clock digits
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = center_x + int(0.85 * clock_radius * math.cos(angle))
        y = center_y + int(0.85 * clock_radius * math.sin(angle))
        digit_text = font.render(str(i), True, BLACK)
        digit_rect = digit_text.get_rect(center=(x, y))
        screen.blit(digit_text, digit_rect)

    # Get current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate angles for hands
    hour_angle = math.radians((hour % 12) * 30 + minute / 2 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    second_angle = math.radians(second * 6 - 90)

    # Draw clock hands
    pygame.draw.line(screen, RED, (center_x, center_y),
                     (center_x + hour_length * math.cos(hour_angle),
                      center_y + hour_length * math.sin(hour_angle)), 8)
    pygame.draw.line(screen, GREEN, (center_x, center_y),
                     (center_x + minute_length * math.cos(minute_angle),
                      center_y + minute_length * math.sin(minute_angle)), 4)
    pygame.draw.line(screen, BLUE, (center_x, center_y),
                     (center_x + second_length * math.cos(second_angle),
                      center_y + second_length * math.sin(second_angle)), 2)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000)

# Quit Pygame
pygame.quit()
sys.exit()