import sys   #使用模块sys中的工具来退出游戏
import pygame
from settings import Settings
'''
class AlienInvasion:
    def __init__(self):
        pygame.init()      #调用本函数来初始化背景设置
        self.screen = pygame.display.set_mode((1200,800))  #显示窗口设置
#赋给self.screen的对象是一个surface。再pygame中surface是屏幕中的一部分，用于显示游戏元素
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)
    def run_game(self):   #此游戏用run_game（）这一方法来控制
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()    #命令pygame让最近绘制的屏幕可见
#该方法包含一个不断运行的while循环
#这个循环包括一个事件循环以及管理屏幕更新的代码。
#时间是用户玩游戏时执行的操作，为程序响应事件可以编写一个事件循环
'''
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):   #此游戏用run_game（）这一方法来控制
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()    #命令pygame让最近绘制的屏幕可见
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
#正确理解是，一种保护性编程模式，它允许一个py文件同时具备可执行脚本和可导入模块的双重身份
