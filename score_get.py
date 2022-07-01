from retrogame.score_tracker import Score
import pygame,async_timeout

pygame.init()
app = pygame.display.set_mode([700,700])
pygame.display.set_caption("Score counter")
score = Score()
font = pygame.font.Font("BACKTO1982.ttf",30)

text = font.render("Score : 1009882",True,(255,255,255),(0,0,0))
textRect = text.get_rect()
textRect.center = (350,350)

while True:
    app.fill((255,255,255))
    app.blit(text,textRect)
    text = font.render(f"Score : {score.getScore()}", True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (350, 350)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
    score.add_point()
