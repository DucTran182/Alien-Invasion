import pygame
from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#Initialize pygame, setting, and screen objective
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Make the Play button
	play_button = Button(ai_settings, screen, "Play")

	#Create an instance to store game statistics
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)

	#Make a ship
	ship = Ship(ai_settings, screen)

	#Make an alien
	alien = Alien(ai_settings, screen)

	#Make a group to store bullets in
	bullets = Group()
	aliens = Group()

	#Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Set background color
	bg_color = (100, 100, 100)

	#Start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, stats, sb, ship, play_button, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()