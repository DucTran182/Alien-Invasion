class Settings():
	def __init__(self):
		#Screen settings
		self.screen_width = 1000
		self.screen_height = 800
		self.bg_color = (100,100,100)
		self.ship_speed_factor = 1.5

		#Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 20
		self.bullet_color = 255, 0, 0

		#Alien settings
		self.alien_speed_factor = 1
		self.ship_limit = 3
		self.fleet_drop_speed = 10

		#How quickly the game speeds up
		self.speedup_scale = 1.1

		#How quickly the alien point values increase
		self.score_scale = 1.5

		self.initialize_dynamic_setting()

	def initialize_dynamic_setting(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		#Fleet direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		#Scoring
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self,alien_points = int(self.alien_points * self.score_scale)