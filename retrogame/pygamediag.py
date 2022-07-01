import random
from tkinter import messagebox

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

from retrogame import sounds 


class App():
    def __init__(self):
        # Sound Initiator
        
        pygame.init()
        
        # sounds.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        
        # Create a custom event for adding a new enemy
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 750)
        
        self.ADDLIFE = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDLIFE, 2000)
        
        self.ADDAPPLE = pygame.USEREVENT + 3
        pygame.time.set_timer(self.ADDAPPLE, 2000)
        
        self.player = sp.Player()
        self.scoretracker = ScoreTracker()
        
        self.enemies = pygame.sprite.Group()
        self.lives = pygame.sprite.Group()
        self.apples = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font("BACKTO1982.ttf",30)

        self.mainloop()
        
        self.after_game()
        
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
                
                elif event.type == self.ADDLIFE:
                    doit = random.randint(0, 1)
                    if self.scoretracker.getLives() < 3 and doit:
                        mylife = sp.Life()
                        self.lives.add(mylife)
                        self.all_sprites.add(mylife)
                
                elif event.type == self.ADDAPPLE:
                    new_apple = sp.Apple()
                    self.apples.add(new_apple)
                    self.all_sprites.add(new_apple)
            
            self.screen.fill((0,0,0))

            text = self.font.render(f"Lives: {self.scoretracker.getLives()} "
                                    f"Score: {self.scoretracker.getScore()}", True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.top = 5
            textRect.left = 5
                    
            pressed_keys = pygame.key.get_pressed()
            
            self.player.update(pressed_keys)
            
            # Update enemy position
            self.enemies.update()
            self.lives.update()
            self.apples.update()
            
            
            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)
            
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                # If so, then remove the player and stop the loop
                #print(self.scoretracker.getLives())
                if self.scoretracker.getLives()==1:
                    self.player.kill()
                    self.scoretracker.save_score()
                    self.scoretracker.close_file()
                    self.running = False
                else:
                    hitlist = pygame.sprite.spritecollide(self.player, self.enemies, False)
                    for element in hitlist:
                        if isinstance(element, sp.Enemies):
                            element.kill()
                    self.scoretracker.rem_life()
                    sounds.stone_sound.play()
            
            if pygame.sprite.spritecollideany(self.player, self.lives):
                # If so, then remove the player and stop the loop
                #print(self.scoretracker.getLives())
                hitlist = pygame.sprite.spritecollide(self.player, self.lives, False)
                for element in hitlist:
                    if isinstance(element, sp.Life):
                        element.kill()
                if self.scoretracker.getLives()<3:
                    self.scoretracker.add_life()
            
            if pygame.sprite.spritecollideany(self.player, self.apples):
                # If so, then remove the player and stop the loop
                #print(self.scoretracker.getLives())
                hitlist = pygame.sprite.spritecollide(self.player, self.apples, False)
                for element in hitlist:
                    if isinstance(element, sp.Friends):
                        element.kill()
                self.scoretracker.add_point()
                sounds.apple_sound.play()

            self.screen.blit(text, textRect)
            pygame.display.flip()
            
            self.clock.tick(500)
        
        # surf, rect = self.create_surface()
        
        # screen.blit(surf, (0, 0))
        # pygame.display.flip()
    
    def after_game(self):
        messagebox.showinfo("End of Game", "The game has ended with score={}".format(
            self.scoretracker.getScore()
        ))
        pygame.quit()
    
    def create_surface(self):
        sf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        rect = self.main_sf.fill((0, 0, 0))
        
        return sf, rect
        
    

def main():
    App()