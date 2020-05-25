import pygame
pygame.init()
gray=(119,118,110) # This is from color picker, combination of RGB
display_width=800
display_height=600
gamedisplays=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Car game")
clock=pygame.time.Clock()

def game_loop():
    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                bumped=True

        gamedisplays.fill(gray)
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()

