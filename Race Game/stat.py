import pygame

class Stat:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.game_running = False
        self.play_button = pygame.Rect(0,0,100,50)
        self.color = (127,127,127)
        self.text_color =  (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        self.text = "Play!"
        self.text_image = self.font.render(self.text, True, self.text_color, self.color)
        self.text_rect = self.text_image.get_rect()
        
    def check(self):
        if not self.game_running:
            self.play_button.center = self.game.screen_rect.center
            self.text_rect.center = self.play_button.center
        if self.game_running:
            self.play_button.bottom = self.game.screen_rect.top
            self.text_rect.center = self.play_button.center

    def draw_button(self):
        self.game.screen.blit(self.text_image, self.text_rect)
        pygame.draw.rect(self.game.screen, self.color, self.play_button)