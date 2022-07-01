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

class App():
    def __init__(self):
        pygame.init()
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
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
                    elif event.key == K_UP:
                        print("Up presssed")
                        # running = False

                # Did the user click the window close button? If so, stop the loop.
                elif event.type == QUIT:
                    self.running = False
    

def main():
    App()