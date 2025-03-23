import pygame
import random

class Border:
    def __init__(self, game, height):
        pygame.init()
        self.rect = pygame.Rect(0,0, game.screen_width, height)
        self.screen = game.screen

    def draw(self):
        pygame.draw.rect(self.screen, (0,0,0), self.rect)

class Obstacle:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.image = pygame.image.load(r"Race Game\images\cone.bmp")
        pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.screen = game.screen
        self.background = game.background
        self.screen_rect = game.screen_rect
        self.rect.x = 1000


    def place(self):
        self.num = random.randint(1, 3)
        if self.num == 1:
            self.rect.bottom = self.screen_rect.height - 60
        if self.num == 2:
            self.rect.centery = self.background.rect.centery
        if self.num == 3:
            self.rect.top = 11

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.speed = self.game.speed
        self.rect.x -= self.speed
        if self.rect.right < self.screen_rect.left:
            self.rect.right = self.screen_rect.right
            self.place()



