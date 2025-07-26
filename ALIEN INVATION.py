import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

player_size = 50
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 60, player_size, player_size)
player_speed = 6

bullets = []
bullet_speed = 8
bullet_cooldown = 400
last_shot_time = 0

alien_size = 40
aliens = []

levels = [
    {"rows": 2, "cols": 5, "speed": 1},
    {"rows": 3, "cols": 6, "speed": 2},
    {"rows": 4, "cols": 7, "speed": 3},
]
current_level = 0
alien_direction = 1

font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def create_aliens(rows, cols, speed):
    alien_list = []
    padding = 10
    offset_x = 50
    offset_y = 50
    for row in range(rows):
        for col in range(cols):
            x = offset_x + col * (alien_size + padding)
            y = offset_y + row * (alien_size + padding)
            alien = pygame.Rect(x, y, alien_size, alien_size)
            alien_list.append(alien)
    return alien_list

aliens = create_aliens(**levels[current_level])

running = True
while running:
    screen.fill(BLACK)
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        now = pygame.time.get_ticks()
        if now - last_shot_time > bullet_cooldown:
            bullet = pygame.Rect(player.centerx - 5, player.top, 10, 20)
            bullets.append(bullet)
            last_shot_time = now

    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    move_down = False
    for alien in aliens:
        alien.x += levels[current_level]["speed"] * alien_direction
        if alien.right >= WIDTH or alien.left <= 0:
            move_down = True

    if move_down:
        alien_direction *= -1
        for alien in aliens:
            alien.y += 20

    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)
                break

    for alien in aliens:
        if alien.bottom >= HEIGHT or alien.colliderect(player):
            draw_text("Game Over!", WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    if not aliens:
        current_level += 1
        if current_level >= len(levels):
            draw_text("You Win!", WIDTH // 2 - 60, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(3000)
            break
        aliens = create_aliens(**levels[current_level])

    pygame.draw.rect(screen, GREEN, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for alien in aliens:
        pygame.draw.rect(screen, RED, alien)

    draw_text(f"Level: {current_level + 1}", 10, 10)
    pygame.display.flip()

pygame.quit()
sys.exit()
