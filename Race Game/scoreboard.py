import pygame
import json

class Scoreboard:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.score = self.game.score
        self.color = (0,0,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        self.text()
        self.high_score()
    
    def text(self):
        score = self.game.score * 100
        text = f"Score: {score:.0f}"
        self.text_image = self.font.render(text, True, self.text_color, self.color)
        self.rect = self.text_image.get_rect()
        self.rect.y = 10
        self.rect.left = 10
    
    def high_score(self):
        high_score = self.game.high_score*100
        text = f"High Score: {high_score:.0f}"
        self.high_tex_img = self.font.render(text, True, self.text_color, self.color)
        self.high_rect = self.high_tex_img.get_rect()
        self.high_rect.left = self.rect.right


    def draw(self):
        self.text()
        self.high_score()
        self.game.screen.blit(self.text_image, self.rect)
        self.game.screen.blit(self.high_tex_img, self.high_rect)
class Stat:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.game_running = False
        self.play_button = pygame.Rect(self.game.screen_width/2,self.game.screen_hieght/2,100,50)
        self.color = (0,0,0)
        self.text_color =  (127,127,127)
        self.font = pygame.font.SysFont(None, 48)
        self.text = "Play!"
        self.text_image = self.font.render(self.text, True, self.text_color, self.color)
        self.text_rect = self.text_image.get_rect()
        self.check()
        
    def check(self):
        if not self.game_running:
            self.play_button.center = self.game.screen_rect.center
            self.text_rect.center = self.game.screen_rect.center
            self.game.score = 0
            self.game.speed = 8
        if self.game_running:
            self.play_button.bottom = self.game.screen_rect.top
            self.text_rect.bottom = self.game.screen_rect.top

    def draw_button(self):
        pygame.draw.rect(self.game.screen, self.color, self.play_button)
        self.game.screen.blit(self.text_image, self.text_rect)