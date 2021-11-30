"""
Discription: 双人外星人入侵游戏主函数，待完善
Play:
    按键 WASD：飞船一方向控制
    按键 P 和 O：飞船一子弹单发
    按键上下左右：飞船二方向控制
    数字键 8：飞船二子弹连发
    数字键 9：飞船二子弹单发
Todolists:
    飞船一未设置碰撞检测
    飞船一未设置子弹连发，飞船二的子弹连发还在测试
    飞船二未设置计分板
    外星人未设置向下移动，只设置了左右移动
"""
import pygame
import game_function as gf

from settings import Settings
from ship import Ship
from ship2 import Ship2
from pygame.sprite import Group
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
#from alien import Alien

def run_game():
	
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	play_button = Button(ai_settings, screen, "Play")
	
	# 创建一艘飞船
	ship = Ship(ai_settings, screen)
	ship2 = Ship2(ai_settings, screen)
	
	# 创建一个用于存储子弹的编组
	bullets = Group()
	bullets2 = Group()
	
	# 创建一个外星人
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens, ship2, bullets2)
	
	# 创建统计游戏统计信息的实例
	stats = Gamestats(ai_settings)
	scoreboard = Scoreboard(ai_settings, screen, stats)
	
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings, stats, screen, ship, bullets, aliens, play_button, scoreboard, ship2, bullets2) # 监视键盘和鼠标事件
		
		if stats.game_active:
			ship.update() # 更新飞船位置
			ship2.update()
			gf.update_bullets(ai_settings, stats, screen, ship, bullets, aliens, scoreboard, ship2, bullets2) # 更新子弹位置	
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, scoreboard, ship2, bullets2)	 # 更新外星人位置
		
		gf.update_screen(ai_settings, stats, screen, ship, bullets, aliens, play_button, scoreboard, ship2, bullets2) # 每次循环都重绘屏幕，伴随着更新屏幕上的图像

if __name__ == '__main__':
    run_game()
