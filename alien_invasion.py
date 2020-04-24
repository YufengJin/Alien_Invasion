import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)
    while True:
        gf.check_events(ship,ai_settings,screen,bullets)
        ship.update()
        gf.update_bullets(bullets,aliens,ai_settings,screen,ship)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)



run_game()