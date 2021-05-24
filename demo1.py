import pygame
import sys

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #initialize game and create screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Train survival")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    # Make an alien.
    
    alien = Alien(ai_settings, screen)
    aliens = Group()
    aliens.add(alien)

    #start the main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        ship.update()
        gf.update_bullets(bullets) 
        bullets.update()
run_game()