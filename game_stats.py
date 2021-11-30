
# 跟踪游戏的统计信息
class Gamestats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

		# 游戏活动状态，决定游戏开始和结束
		self.game_active = False
		
		# 最高得分
		self.high_score = 0
		
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		
		
	
