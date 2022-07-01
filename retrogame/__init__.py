import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from retrogame.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
import retrogame.sprites as sp
from retrogame.score_tracker import Score as ScoreTracker


class App():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        
        # Create a custom event for adding a new enemy
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 750)
        
        self.player = sp.Player()
        self.scoretracker = ScoreTracker()
        
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        
        self.clock = pygame.time.Clock()

        self.mainloop()
        
    def mainloop(self):
        # Variable to keep the main loop running
        self.running = True

        # Main loop
        while self.running:
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:
                    
                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        self.running = False
                    # elif event.key == K_UP:
                        # print("Up presssed")
                        # running = False

                # Did the user click the window close button? If so, stop the loop.
                elif event.type == QUIT:
                    self.running = False
                    
                # Add a new enemy?
                elif event.type == self.ADDENEMY:
                    # Create the new enemy and add it to sprite groups
                    new_enemy = sp.Stone()
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
            
            self.screen.fill((0,0,0))
                    
            pressed_keys = pygame.key.get_pressed()
            
            self.player.update(pressed_keys)
            
            # Update enemy position
            self.enemies.update()
        
            
            
            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)
            
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                # If so, then remove the player and stop the loop
                #print(self.scoretracker.getLives())
                if self.scoretracker.getLives()==0:
                    self.player.kill()
                    self.running = False
                else:
                    hitlist = pygame.sprite.spritecollide(self.player, self.enemies, False)
                    for element in hitlist:
                        if isinstance(element, sp.Stone):
                            element.kill()
                    self.scoretracker.rem_life()
            
            
            pygame.display.flip()
            
            self.clock.tick(500)
        
        # surf, rect = self.create_surface()
        
        # screen.blit(surf, (0, 0))
        # pygame.display.flip()
    
    def create_surface(self):
        sf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        rect = self.main_sf.fill((0, 0, 0))
        
        return sf, rect
        
    

def main():
    App()