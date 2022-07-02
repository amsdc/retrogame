import random

import pygame

from pygame.locals import (
    RLEACCEL,
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

class Enemies():
    """Base class for enemies"""
    pass

class Friends():
    """Base class for friends"""
    pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.player_width = 75
        self.player_height = 75
        
        self.p_left_padding = 5
        self.p_right_padding = 5
        self.p_bottom_padding = 5
        
        # self.surf = pygame.Surface((self.player_width, self.player_height))
        # self.surf.fill((245,27,2))
        self.surf = pygame.image.load("img/angryball.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        
        # Position our player in center
        self.rect.left = (SCREEN_WIDTH/2)-(self.player_width/2)
        self.rect.top = (SCREEN_HEIGHT)-(self.player_height)
    
    def update(self, pressed_keys):
        # if pressed_keys[K_UP]:
            # # print("UP")
            # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
            # # print("DN")
            # self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1.5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1.5, 0)
            
        # Keep player on the screen
        if self.rect.left < self.p_left_padding:
            self.rect.left = self.p_left_padding
        if self.rect.right > SCREEN_WIDTH-self.p_right_padding:
            self.rect.right = SCREEN_WIDTH-self.p_right_padding
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT-self.p_bottom_padding:
            self.rect.bottom = SCREEN_HEIGHT-self.p_bottom_padding


class Stone(pygame.sprite.Sprite, Enemies):
    def __init__(self):
        super().__init__()
        self.player_width = 75
        self.player_height = 75
        
        self.s_left_padding = 5
        self.s_right_padding = 5
        self.s_bottom_padding = 5
        
        #self.surf = pygame.Surface((self.player_width, self.player_height))
        pichoice = random.choice(["stone.png", "stone2.png"])
        self.surf = pygame.image.load("img/{}".format(pichoice)).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # pygame.transform.scale(self.surf, (self.player_width, self.player_height))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0+self.s_left_padding, SCREEN_WIDTH-self.s_right_padding),
                random.randint(-100, -20),
            )
        )
        
        # self.rect.left = 750
        # self.rect.top = random.randint(-100, -20)
        
        self.speed = random.randint(1, 3)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT-self.s_bottom_padding:
            self.kill()

class Life(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_width = 75
        self.player_height = 75
        
        self.s_left_padding = 5
        self.s_right_padding = 5
        self.s_bottom_padding = 5
        
        #self.surf = pygame.Surface((self.player_width, self.player_height))
        self.surf = pygame.image.load("img/heart.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # pygame.transform.scale(self.surf, (self.player_width, self.player_height))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0+self.s_left_padding, SCREEN_WIDTH-self.s_right_padding),
                random.randint(-100, -20),
            )
        )
        self.speed = random.randint(1, 3)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT-self.s_bottom_padding:
            self.kill()

class Apple(pygame.sprite.Sprite, Friends):
    def __init__(self):
        super().__init__()
        self.player_width = 75
        self.player_height = 75
        
        self.s_left_padding = 5
        self.s_right_padding = 5
        self.s_bottom_padding = 5
        
        #self.surf = pygame.Surface((self.player_width, self.player_height))
        self.surf = pygame.image.load("img/apple.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # pygame.transform.scale(self.surf, (self.player_width, self.player_height))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0+self.s_left_padding, SCREEN_WIDTH-self.s_right_padding),
                random.randint(-100, -20),
            )
        )
        self.speed = random.randint(1, 3)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT-self.s_bottom_padding:
            self.kill()