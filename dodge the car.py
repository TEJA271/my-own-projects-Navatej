import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodging Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
BLUE = (50, 50, 255)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

road_line_y = 0

player = pygame.Rect(WIDTH // 2 - 30, HEIGHT - 140, 60, 120)
player_speed = 6

enemy_cars = []
num_enemies = 3
enemy_speed = 5

score = 0
game_over = False

def spawn_enemies():
    for _ in range(num_enemies):
        x = random.randint(50, WIDTH - 110)
        y = random.randint(-800, -100)
        enemy_cars.append(pygame.Rect(x, y, 60, 120))

def reset_game():
    global player, enemy_cars, score, enemy_speed, game_over
    player.x = WIDTH // 2 - 30
    enemy_cars.clear()
    spawn_enemies()
    score = 0
    enemy_speed = 5
    game_over = False

def draw_road():
    global road_line_y
    screen.fill(GRAY)

    pygame.draw.rect(screen, WHITE, (40, 0, 10, HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 50, 0, 10, HEIGHT))

    for i in range(20):
        pygame.draw.rect(screen, YELLOW, (WIDTH // 2 - 5, road_line_y + i * 40, 10, 20))

    road_line_y += 5
    if road_line_y > 40:
        road_line_y = 0

def draw_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def show_game_over():
    over_text = font.render("Game Over! Press R to Restart", True, RED)
    screen.blit(over_text, (50, HEIGHT // 2))

spawn_enemies()
running = True  


while running:
    clock.tick(60)
    draw_road()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        if keys[pygame.K_LEFT] and player.x > 50:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - 110:
            player.x += player_speed

        pygame.draw.rect(screen, BLUE, player)

        for enemy in enemy_cars:
            enemy.y += enemy_speed
            pygame.draw.rect(screen, RED, enemy)

            if player.colliderect(enemy):
                game_over = True

            if enemy.y > HEIGHT:
                enemy.y = random.randint(-800, -100)
                enemy.x = random.randint(50, WIDTH - 110)
                score += 1
                if score % 5 == 0:
                    enemy_speed += 0.3

        draw_score()
    else:
        show_game_over()
        if keys[pygame.K_r]:
            reset_game()

    pygame.display.flip()

pygame.quit()
sys.exit()

