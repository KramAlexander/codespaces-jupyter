import pygame
import time
import random

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
snake_size = 1
snake_speed = GRID_SIZE
score = 0

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK=(0,0,0)
BLUE = (0,0,255)
# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize snake
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = (0, 0)

# Initialize food
food_pos = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
            random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)

# Game loop
clock = pygame.time.Clock()
game_over = False
    
start_time = time.time()
background = pygame.image.load("/Users/alexanderkram/Library/Mobile Documents/com~apple~CloudDocs/codespaces-jupyter/snakes/37716068933bae2f9b11ff90bc91b015.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))          

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, snake_speed):
                snake_direction = (0, -snake_speed)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -snake_speed):
                snake_direction = (0, snake_speed)
            elif event.key == pygame.K_LEFT and snake_direction != (snake_speed, 0):
                snake_direction = (-snake_speed, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-snake_speed, 0):
                snake_direction = (snake_speed, 0)

    # Move the snake
    new_head = ((snake[0][0] + snake_direction[0]) % WIDTH, (snake[0][1] + snake_direction[1]) % HEIGHT)
    snake.insert(0, new_head)

    # Check for collisions with food
    if new_head == food_pos:
        score += 1
        food_pos = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    else:
        snake.pop()

    # Check for collisions with itself
    if new_head in snake[1:]:
        game_over = True

    # Draw everything
    #screen.fill(BLACK)
    screen.blit(background, (0, 0))
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, BLUE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

    # Display score
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Get the current time
    current_time = time.time()

    # Calculate the elapsed time
    elapsed_time = current_time - start_time
    pygame.display.flip()

    # Set the frame rate
    clock.tick(15)

print(f"You survived {elapsed_time} seconds")
pygame.quit()
