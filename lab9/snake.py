import pygame
import time
import random

pygame.init()


WIDTH = 680
HEIGHT = 440


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.display.set_caption('Zhylanchick')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
fps = pygame.time.Clock()

# Initial snake position and body
snake_position = [100, 50]
snake_body = [[100, 50], [80, 50], [60, 50]]
direction = 'RIGHT'
change_to = direction


score = 0
level = 1
snake_speed = 13

# Fruit variables
fruit_position = [random.randrange(1, (WIDTH // 10)) * 10,
                  random.randrange(1, (HEIGHT // 10)) * 10]
fruit_weight = random.choice([1, 2, 3])   # Random weight (score multiplier)
fruit_timer = pygame.time.get_ticks()     # Time when fruit was spawned
fruit_lifespan = 5000                     # Fruit disappears after 5 seconds
fruit_spawn = True

# Score and level display function
def show_info(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}  Level: {level}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Game Over screen
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Prevent the snake from reversing
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Insert new position
    snake_body.insert(0, list(snake_position))

    # Check if fruit is eaten
    if snake_position == fruit_position:
        score += fruit_weight * 10
        fruit_spawn = False

        # Increase level and speed every 60 points
        if score // (level * 60) > 0:
            level += 1
            snake_speed += 2
    else:
        snake_body.pop()

    # Handle fruit disappearance after lifespan
    current_time = pygame.time.get_ticks()
    if current_time - fruit_timer > fruit_lifespan:
        fruit_spawn = False

    # Spawn a new fruit if needed
    if not fruit_spawn:
        while True:
            fruit_position = [random.randrange(1, (WIDTH // 10)) * 10,
                              random.randrange(1, (HEIGHT // 10)) * 10]
            if fruit_position not in snake_body:
                break
        fruit_weight = random.choice([1, 2, 3])  # Assign random weight again
        fruit_timer = pygame.time.get_ticks()    # Reset spawn timer
        fruit_spawn = True

    # Fill background
    game_window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, blue, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw fruit (color based on weight)
    fruit_color = green if fruit_weight == 1 else (255, 165, 0) if fruit_weight == 2 else red
    pygame.draw.rect(game_window, fruit_color, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Wall collision
    if snake_position[0] < 0 or snake_position[0] >= WIDTH:
        game_over()
    if snake_position[1] < 0 or snake_position[1] >= HEIGHT:
        game_over()

    # Self collision
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Show score and level
    show_info(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)