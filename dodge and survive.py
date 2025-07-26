import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge and Survive")
clock = pygame.time.Clock()

player_size = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 10, player_size, player_size)
player_speed = 7

obstacle_width = 50
obstacle_height = 50

levels = [
    {"speed": 3, "spawn_delay": 1500},
    {"speed": 5, "spawn_delay": 1000},
    {"speed": 7, "spawn_delay": 800}
]
current_level = 0
obstacles = []
level_start_time = pygame.time.get_ticks()
level_duration = 15_000  # 15 seconds per level

font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def spawn_obstacle():
    x = random.randint(0, WIDTH - obstacle_width)
    rect = pygame.Rect(x, 0, obstacle_width, obstacle_height)
    obstacles.append(rect)

SPAWN_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBSTACLE, levels[current_level]["spawn_delay"])

running = True
while running:
    screen.fill(BLACK)
    time_now = pygame.time.get_ticks()

    if time_now - level_start_time > level_duration:
        current_level += 1
        if current_level >= len(levels):
            draw_text("You Win!", WIDTH // 2 - 80, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            break
        level_start_time = time_now
        pygame.time.set_timer(SPAWN_OBSTACLE, levels[current_level]["spawn_delay"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_OBSTACLE:
            spawn_obstacle()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    for obstacle in obstacles[:]:
        obstacle.y += levels[current_level]["speed"]
        if obstacle.colliderect(player):
            draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        if obstacle.top > HEIGHT:
            obstacles.remove(obstacle)
        pygame.draw.rect(screen, RED, obstacle)

    pygame.draw.rect(screen, WHITE, player)

    draw_text(f"Level: {current_level + 1}", 10, 10)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
