
import pygame
from pygame.sprite import Sprite

class Ship2(Sprite):
	
	def __init__(self, ai_settings, screen):
		""" 初始化飞船并设置其初始位置 """
		super(Ship2, self).__init__()
		self.screen =screen
		self.ai_settings = ai_settings
		
		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# 将每艘新飞船放在屏幕底部中央
		self.center = float(self.screen_rect.centerx)
		self.bottoms = float(self.screen_rect.bottom)
		self.center -=40
		#self.bottoms -= 100
		
		# 该语句是为了在游戏开始时将飞船放置在底部中央，如果无该语句则飞船会在左上角
		self.rect.centerx = self.center
		self.rect.bottom = self.bottoms
		
		# 移动标志
		self.moving_right = False
		self.moving_left = False		
		self.moving_up = False
		self.moving_down = False
		
		self.flag = False # 控制子弹是否持续发射
		
	def blitme(self):
		""" 在指定位置绘制飞船 """
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		""" 根据移动标志调整飞船的位置 """
		if self.moving_right and self.rect.right < self.screen_rect.right: # 向右
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0: # 向左
			self.center -= self.ai_settings.ship_speed_factor
			
		if self.moving_up and self.rect.top > 0: # 向上
			self.bottoms -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom: # 向下
			self.bottoms += self.ai_settings.ship_speed_factor
		#if self.conti:
			
		# 根据self.center更新rect对象
		self.rect.centerx = self.center
		self.rect.bottom = self.bottoms
	
	# 重置飞船位置
	def center_ship(self):
		self.center = self.screen_rect.centerx-40
		self.bottoms = self.screen_rect.bottom





