import pygame

WIDTH = 1000
HEIGHT = 700
white = (255, 255, 255)
red = (255, 0, 0)
brown = (153,121,80)
grass_green = (46,139,87)
sky_blue = (136,206,235)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('My Pygame Window')
screen.fill(sky_blue)
pygame.draw.rect(screen, brown, (0,630, 1000, 70))
pygame.draw.rect(screen,grass_green, (0, 610, 1000, 20))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()