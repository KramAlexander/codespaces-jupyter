import pygame
import random

pygame.init()
# declaring propetries of my game (size and colors)
WIDTH = 1000
HEIGHT = 700
white = (255, 255, 255)
red = (255, 0, 0)
brown = (153, 121, 80)
green_grass = (46, 139, 87)
sky_blue = (136, 206, 235)

# loading images
bird_image = pygame.image.load("/Users/alexanderkram/Library/Mobile Documents/com~apple~CloudDocs/codespaces-jupyter/Games/flappybird/flappybird/Bird.png")
pipe_image = pygame.image.load("/Users/alexanderkram/Library/Mobile Documents/com~apple~CloudDocs/codespaces-jupyter/Games/flappybird/flappybird/IMG_0401-removebg-preview.png")
pipe_rect = pipe_image.get_rect()

# bird-basics
bird_width = 60
bird_height = 45
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_velocity = 0

# pipe-basics
pipe_width = pipe_rect.width
pipe_height = pipe_rect.width
pipe_gap = 200
pipes = []
spawn_interval = 100  # Adjust as needed

# constants
FPS = 70
GRAVITY = 0.5
JUMP_HEIGHT = 10

# initialze screen and set the caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')


clock = pygame.time.Clock()
running = True
frame_count = 0

# drawing the bird (adjusted)
def draw_bird():
    small_bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
    screen.blit(small_bird_image, (bird_x, int(bird_y)))

# class for creating, moving and drawing the pipes through image
class Pipe:
    def __init__(self, x):
        self.x = x
        self.upper_pipe_height = random.randint(150, 450)
        self.lower_pipe_height = HEIGHT - self.upper_pipe_height - pipe_gap
        self.pipe_image_upper = pygame.transform.scale(pipe_image, (pipe_width, self.upper_pipe_height))
        self.pipe_image_lower = pygame.transform.scale(pipe_image, (pipe_width, self.lower_pipe_height))
        self.pipe_width = self.pipe_image_upper.get_width()  # Get the actual width of the scaled image

    def move(self):
        self.x -= 5

    def draw(self):
        screen.blit(self.pipe_image_upper, (self.x, 0))
        screen.blit(self.pipe_image_lower, (self.x, HEIGHT - self.lower_pipe_height))
# checks if the flappy collides with a pipe
def collision_with_pipe():
    for pipe in pipes:
        # lower or higher pipe
        if (
            bird_x < pipe.x + pipe.pipe_width
            and bird_x + bird_width > pipe.x
            and (bird_y < pipe.upper_pipe_height or bird_y + bird_height > HEIGHT - pipe.lower_pipe_height)
        ):
            print("Collision detected!")
            print(f"bird_x: {bird_x}, bird_y: {bird_y}")
            print(f"pipe.x: {pipe.x}, pipe.upper_pipe_height: {pipe.upper_pipe_height}, pipe.lower_pipe_height: {pipe.lower_pipe_height}")
            return True
    return False

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -JUMP_HEIGHT

    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # spawn the pipes
    if frame_count % spawn_interval == 0:
        new_pipe = Pipe(WIDTH)
        pipes.append(new_pipe)

    # remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x + pipe.pipe_width > 0]

    screen.fill(sky_blue)

    # move and draw pipes
    for pipe in pipes:
        pipe.move()
        pipe.draw()

    # drawing the background
    pygame.draw.rect(screen, brown, (0, 630, 1000, 70))
    pygame.draw.rect(screen, green_grass, (0, 610, 1000, 20))
    
    draw_bird()

    # checking for collision
    if collision_with_pipe():
        running = False

    pygame.display.flip()
    clock.tick(FPS)
    frame_count += 1

pygame.quit()
