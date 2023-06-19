import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

ground_surface = pygame.image.load('platformer_resources/ground.png')
ground_surface = pygame.transform.scale(ground_surface, (800,120))

sky_surface = pygame.Surface((800,500))
sky_surface.fill('aquamarine3')

text_font = pygame.font.Font(None, 50)
text_surface = text_font.render("Let's Go!", False, "coral")

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,480))
    screen.blit(text_surface, (330, 100))
    
    pygame.display.update()
    clock.tick(60)
