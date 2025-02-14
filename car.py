import pygame

class Car:
    def __init__(self, game):
        pygame.init()
        self.image = pygame.image.load(r'Race Game\images\car.bmp')
        self.rect = self.image.get_rect()
        self.screen = game.screen
        self.color = (0,0,0)
        self.screen_rect = self.screen.get_rect()
        self.rect.left = 10
        self.rect.centery = game.screen_hieght/2
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up == True:
            self.rect.y -= 7
        if self.moving_down == True:
            self.rect.y += 7
