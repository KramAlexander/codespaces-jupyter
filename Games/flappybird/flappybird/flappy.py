import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 700
white = (255, 255, 255)
red = (255, 0, 0)
brown = (153,121,80)
green_grass = (46,139,87)
sky_blue = (136,206,235)

# Bird properties
bird_width = 60  # Adjust the width to make the bird smaller
bird_height = 45  # Adjust the height to make the bird smaller
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_velocity = 0
# Constants
FPS = 60
GRAVITY = 0.5
JUMP_HEIGHT = 10

bird_image = pygame.image.load("/Users/alexanderkram/Library/Mobile Documents/com~apple~CloudDocs/codespaces-jupyter/Games/flappybird/flappybird/Bird.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('My Pygame Window')

screen.fill(sky_blue)
pygame.draw.rect(screen, brown, (0,630, 1000, 70))
pygame.draw.rect(screen,green_grass, (0, 610, 1000, 20))

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -JUMP_HEIGHT
   
        # Update bird position
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    screen.fill(sky_blue)

    # Draw the ground and grass
    pygame.draw.rect(screen, brown, (0, 630, 1000, 70))
    pygame.draw.rect(screen, green_grass, (0, 610, 1000, 20))
    
    # bird
    small_bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
    screen.blit(small_bird_image, (bird_x, int(bird_y)))
    pygame.display.flip()

pygame.quit()