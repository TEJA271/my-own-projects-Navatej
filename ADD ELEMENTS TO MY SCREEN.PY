import pygame
import sys

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My First Game Screen")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
text_surface = font.render('Welcome to My First Game Screen!', True, BLACK)
text_rect = text_surface.get_rect(center=(screen_width // 2, 50))

rect_width = 100
rect_height = 60
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rect)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
