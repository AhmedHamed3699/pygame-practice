import pygame
from sys import exit

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

ground_surface = pygame.image.load('platformer_resources/ground.png')
ground_surface = pygame.transform.scale(ground_surface, (800,120))

sky_surface = pygame.Surface((800,500))
sky_surface.fill('cyan3')

clouds_surface = pygame.image.load("platformer_resources/clouds.png")
clouds_surface = pygame.transform.scale(clouds_surface, (550,150))


text_font = pygame.font.Font(None, 30)
text_surface = text_font.render("Once Upon A Time ...", False, "darkblue")

clouds_pos = 200

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
            
    if clouds_pos == -580:
        clouds_pos = 800

    clouds_pos -= 2
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,480))
    screen.blit(text_surface, (20, 20))
    screen.blit(clouds_surface, (clouds_pos, 60))
    
    pygame.display.update()
    clock.tick(60)
