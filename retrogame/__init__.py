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


class App():
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.player = sp.Player()
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
                    
            pressed_keys = pygame.key.get_pressed()
            
            self.player.update(pressed_keys)
        
            self.screen.fill((0,0,0))
            
            self.screen.blit(self.player.surf, self.player.rect)
            
            
            
            pygame.display.flip()
        
        # surf, rect = self.create_surface()
        
        # screen.blit(surf, (0, 0))
        # pygame.display.flip()
    
    def create_surface(self):
        sf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        rect = self.main_sf.fill((0, 0, 0))
        
        return sf, rect
        
    

def main():
    App()