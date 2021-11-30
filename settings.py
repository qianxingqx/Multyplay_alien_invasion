
class Settings():
	"""
	存储游戏中的所有设置的类
	"""
	
	def __init__(self):
		""" 初始化游戏的设置 """
		
		# 屏幕设置		
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230, 230, 230) # RGB
		
		# 飞船的设置
		self.ship_limit = 3
		
		# 子弹设置
		self.bullet_width = 5
		self.bullet_height = 10
		self.bullet_color = 60, 60, 60
		self.bullets_num = 1000 # 限制子弹数量
		
		# 外星人设置
		self.fleet_drop_speed = 0 # 向下移动
		self.fleet_direction = 1 # 为1表示右移，为-1表示左移
		
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		
		self.init_dynamic()
		
	def init_dynamic(self):
		# 用于在重新开始后重置参数
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed = 1
		
		# 计分
		self.alien_points = 10
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		#print(self.alien_points)
		
