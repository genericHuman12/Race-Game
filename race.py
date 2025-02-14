import pygame
import sys
from car import Car
from background import Background
from obstacles import Border, Obstacle

class Race:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_hieght = self.screen_rect.height
        self.car = Car(self)
        self.background = Background(self)
        self.border1 = Border(self, 10)
        self.border2 = Border(self, 60)
        self.border2.rect.bottom = self.screen_rect.bottom
        self.obstacle = Obstacle(self)
        self.obstacle.place()

    def run_game(self):
        while True:
            self.check_events()
            self.background.scroll_screen()
            self.obstacle.update()
            self.check_car()
            self.check_collisoins()
            self.car.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill('white')
        self.background.draw()
        self.border1.draw()
        self.border2.draw()
        self.obstacle.draw()
        self.car.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)

    def keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.car.moving_down = False
        elif event.key == pygame.K_UP:
            self.car.moving_up = False

    def keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.car.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.car.moving_down = True

    def check_car(self):
        if self.car.rect.top == self.border1.rect.bottom:
            self.car.moving_up = False
        if self.car.rect.bottom == self.border2.rect.top:
            self.car.moving_down = False

    def check_collisoins(self):
        car_collide = self.car.rect.colliderect(self.obstacle.rect)
        if car_collide:
            sys.exit()

race = Race()
race.run_game()