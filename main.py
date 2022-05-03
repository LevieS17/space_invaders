# import pygame and system features
# Levi Shoaff

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from button import Button

# define main game function
def alien_invasion():
    # initialization pygame library
    pygame.init()
    # access settings
    settings = Settings()
    # create a display by inputting width and height of display
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    # names the displayed screen
    pygame.display.set_caption('Alien Invasion')
    # add ship
    ship = Ship(screen)

    # Make a play button
    play_button = Button(settings, screen, "Play Game")

    # make a group to store bullets in
    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    # Updates bullet
    bullets.update()

    # loop to start animation
    while True:

        # access event handler from game functions
        gf.check_events(settings, screen, ship, bullets, play_button)

        bullets.update()

        #updates screen
        gf.update_screen(settings, screen, ship, bullets, aliens, play_button)



alien_invasion()
