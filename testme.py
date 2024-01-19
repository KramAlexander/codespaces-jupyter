import pygame
import sys

# Initialize Pygame
pygame.init()

# Set display size based on your 3.5-inch display resolution
width, height = 320, 480
screen = pygame.display.set_mode((width, height))

# Fill the screen with a color (optional)
screen.fill((255, 255, 255))

# Update the display
pygame.display.flip()

# Run an event loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()