import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

ground_surface = pygame.image.load('Platformer_2/ground.png')
ground_surface = pygame.transform.scale(ground_surface, (800,120))

sky_surface = pygame.Surface((800,500))
sky_surface.fill('aquamarine3')

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,480))
    
    pygame.display.update()
    clock.tick(60)
