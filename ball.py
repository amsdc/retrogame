from ball_class import *
pygame.init()

main_screen = pygame.display.set_mode([700,700])
pygame.display.set_caption("Retro-Game")
game_end = False
ball = Ball()
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
    main_screen.fill((255,255,255))
    main_screen.blit(ball.surf,(350-ball.size/2,350-ball.size/2))
    pygame.display.flip()
pygame.quit()
