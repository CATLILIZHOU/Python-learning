import pygame
class Ship:       #管理飞船的类
    def __init__(self,ai_game):    #初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
#加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
#对于每艘飞船，都将其放在屏幕底部中央
        self.rect.midbottom =  self.screen_rect.midbottom
    def blitme(self):
        self.screen.blilt(self.image,self.rect)
#pygame之所以搞笑，是因为它将所有游戏元素可以让你当成矩形来处理，而玩家实际上很难发现这一点
#类似于bottom,top,canter,midleft是经常用到的来确认surface位置的一些方法


