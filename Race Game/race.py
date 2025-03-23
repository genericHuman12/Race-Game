import pygame
import sys
from car import Car
from background import Background
from obstacles import Border, Obstacle
from scoreboard import Scoreboard, Stat

class Race:
    def __init__(self):
        pygame.init()
        self.speed = 8
        self.score = 0
        self.high_score = 0
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
        self.obstacle2 = Obstacle(self)
        self.scoreboard = Scoreboard(self)
        self.obstacle2.place()
        self.obstacle.place()
        self.stats = Stat(self)

    def run_game(self):
        while True:
            self.stats.check()
            self.check_events()
            self.background.scroll_screen()
            self.obstacle.update()
            self.obstacle2.update()
            if self.stats.game_running:
                self.update_score()
                self.check_car()
                self.car.update()
            self.update_screen()

    def update_screen(self):
        self.screen.fill('white')
        self.background.draw()
        self.border1.draw()
        self.border2.draw()
        self.scoreboard.draw()
        self.obstacle.draw()
        self.obstacle2.draw()
        self.car.draw()
        self.stats.draw_button()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.mouse_events(mouse_pos)

    def mouse_events(self, mouse_pos):
        play_button_click = self.stats.play_button.collidepoint(mouse_pos)
        if play_button_click:
            self.stats.game_running =True
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
        top_border_collide = self.car.rect.colliderect(self.border1.rect)
        if top_border_collide:
            self.car.moving_up = False
        bottom_border_collide = self.car.rect.colliderect(self.border2.rect)
        if bottom_border_collide:
            self.car.moving_down = False
        car_collide = self.car.rect.colliderect(self.obstacle.rect) or self.car.rect.colliderect(self.obstacle2.rect)
        if car_collide:
            self.stats.game_running = False
    
    def update_score(self):
        self.score += 0.01
        self.score = round(self.score, 2)
        if self.score//1 == 0:
            self.speed *= 1.0115
        if self.score > self.high_score:
            self.high_score = self.score
        if self.score > self.high_score:
            self.high_score = self.score

race = Race()
race.run_game()