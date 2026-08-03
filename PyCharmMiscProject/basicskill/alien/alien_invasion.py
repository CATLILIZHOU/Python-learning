import sys   #使用模块sys中的工具来退出游戏
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
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
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
#创建屏幕时，传入了尺寸（0，0）以及后续fullscreen的参数
#由于无法预先知道屏幕的宽度与高度，因此要在创建屏幕后来更新这些设置
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)


    def run_game(self):   #此游戏用run_game（）这一方法来控制
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()  #十分bug的是，如果此时你的输入法是中文的话，这一条不好使
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # 剔除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()  # 命令pygame让最近绘制的屏幕可见

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
#正确理解是，一种保护性编程模式，它允许一个py文件同时具备可执行脚本和可导入模块的双重身份
#响应按键，在pygame中注册时间。事件都是通过pygame.event.get()
