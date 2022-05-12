import pygame

class Ship():

    def __init__(self, screen):

        # load image of ship and access image data
        self.image = pygame.image.load('Images/rocket(alien_invasion).png')
        # resize
        self.image = pygame.transform.scale(self.image, (50,50))
        # tells computer to interpret self.image as a rectangle
        self.rect = self.image.get_rect()
        # tells computer to interpret screen as a rectangle
        self.screen_rect = screen.get_rect()
        self.screen = screen

        # set starting location of each ship
        # makes center x value of ship the same as the center x value of the screen
        self.rect.centerx = self.screen_rect.centerx

        # makes the bottom of the ship the same as the bottom of the screen
        self.rect.bottom = self.screen_rect.bottom

        # stores center x of ship as a decimal value
        self.center = float(self.rect.centerx)

        # create movement flags to determine if the ship is moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # draw the ship on the screen
        # Image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    # Moves ship up/down/left/right and sets walls
    def update(self, settings):
        # Sets walls and moves ships for the right of the screen
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += settings.ship_speed
        # Sets walls and moves ships for the left of the screen.
        if self.moving_left and self.rect.left >= 0:
            self.center -= settings.ship_speed
        # Set walls and moves ships for the top of the screen
        if self.moving_up and self.rect.top >= 0:
            self.rect.centery -= settings.ship_speed
        # Sets walls and moves ships for the bottom of the screen
        if self.moving_down and self.rect.bottom <= 600:
            self.rect.centery += settings.ship_speed

        # set center of the rectangle of the x and y for the center of the screen
        self.rect.centerx = self.center





