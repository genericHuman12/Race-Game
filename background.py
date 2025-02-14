import pygame
import math

class Background:
    def __init__(self, game):
        pygame.init()
        self.screen  = game.screen
        self.image = pygame.image.load(r'Race Game\images\track.bmp')
        self.tiles = math.ceil(game.screen_width / self.image.get_width()) + 2
        self.clock = pygame.time.Clock()
        self.scroll = 0
        self.rect = self.image.get_rect()

    def scroll_screen(self):
        self.clock.tick(33)  
        self.i = 0
        # FRAME FOR SCROLLING 
        self.scroll -= 15
    
        # RESET THE SCROLL FRAME 
        if abs(self.scroll) > self.image.get_width(): 
            self.scroll = 0

    def draw(self):
        while(self.i < self.tiles): 
            self.screen.blit(self.image, (self.image.get_width()*self.i 
                            + self.scroll, 0)) 
            self.i += 1

        