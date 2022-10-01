# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group


import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建用于存储子弹的Group
    bullets = Group()

    while True:
        print("main loop go on!")
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()  # 更新飞船状态
        bullets.update() # 更新子弹状态
        gf.update_screen(ai_settings, screen, ship, bullets)  # 绘制屏幕


if __name__ == '__main__':
    run_game()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
