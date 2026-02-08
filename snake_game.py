import pygame
import time
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE  = (50, 153, 213)

# Screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

font = pygame.font.SysFont("bahnschrift", 25)

# Display score
def show_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Draw snake
def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], block, block])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    dx = dy = 0

    snake = []
    length = 1

    foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
    foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press C-Play Again or Q-Quit", True, RED)
            screen.blit(msg, [WIDTH / 8, HEIGHT / 3])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, SNAKE_BLOCK

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x, y]
        snake.append(snake_head)
        if len(snake) > length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake)
        show_score(length - 1)
        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randrange(0, WIDTH - SNAKE_BLOCK, 10)
            foody = random.randrange(0, HEIGHT - SNAKE_BLOCK, 10)
            length += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
