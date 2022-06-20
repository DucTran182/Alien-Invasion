class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		#Start Alien Invasion in a active state
		self.game_active = True

		#Start game in an inactive state
		self.game_active = False

		#High score should nver be reset
		self.high_score = 0

	def reset_stats(self):
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0 
		self.level = 1

