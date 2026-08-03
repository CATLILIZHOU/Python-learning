import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        #在（0,0)出创建一个表示子弹的矩形，再设置一个正确的位置
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)   #存储用小数来表示的子弹位置，y坐标存储为小数值方便微调子弹速度

    def update(self):
        self.y -= self.settings.bullet_speed    #更新表示子弹位置的小数值
        self.rect.y = self.y    #更新表示子弹的rect的位置

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        