
import pygame
from pygame.sprite import Sprite

# Bullet类继承了从模块pygame.sprite中导入的Sprite类，通过使用精灵，可以将游戏中的相关元素编组
# 子弹并非基于图像的，而是创建的一个矩形
class Bullet2(Sprite):
	""" 一个对飞船发射的子弹进行管理的类 """
	
	def __init__(self, ai_settings, screen, ship2):
		""" 在飞船所处位置创建一个子弹对象 """
		# 调用super来继承Sprite
		super(Bullet2, self).__init__()
		self.screen = screen
		
		# 在(0,0)出创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
								ai_settings.bullet_height)
								
		self.rect.centerx = ship2.rect.centerx
		self.rect.top = ship2.rect.top
		
		# 存储用小数表示的子弹位置
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
		
	
	# 子弹位置
	def update(self):
		""" 向上移动子弹 """
		
		# 更新表示子弹位置的小数值
		self.y -= self.speed_factor
		# 更新表示子弹的rect的位置
		self.rect.y = self.y
		
	# 在屏幕上绘制子弹
	def draw_bullet(self):
		""" 在屏幕上绘制子弹 """
		pygame.draw.rect(self.screen, self.color, self.rect)










