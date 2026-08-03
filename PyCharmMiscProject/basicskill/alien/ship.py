import pygame
class Ship:       #管理飞船的类
    def __init__(self,ai_game):    #初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) #rect只能存储该值的整数部分，使用float将其值转换为小数
        self.moving_right = False
        self.moving_left = False
#对于每艘飞船，都将其放在屏幕底部中央
        self.rect.midbottom =  self.screen_rect.midbottom
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image,self.rect)
#pygame之所以搞笑，是因为它将所有游戏元素可以让你当成矩形来处理，而玩家实际上很难发现这一点
#类似于bottom,top,canter,midleft是经常用到的来确认surface位置的一些方法



