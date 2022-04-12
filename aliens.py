import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    #A class to represent a single alien in the alien fleet
    def __init__(self, settings, screen):
        super(Alien, self).__init__()

        # define attributes screen and settings
        self.screen = screen
        self.settings = settings

        # load alien ship image and scale it to fit screen
        self.image = pygame.image.load('Images/alien(alien_invasion).png') # loads image of alien ship form directory
        self.image = pygame.transform.scale(self.image, (80,40)) # scales alien ship
        self.rect = self.image.get_rect()

        #set starting location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        # spacing for the fleet
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

        self.speed = 1
        self.direction = 1


    def blitme(self):
        # draw the alien on the screen
        # Image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)

    def update(self):
        #move alien
        self.x += self.speed * self.direction
        self.rect.x = self.x

    def check_wall(self):
        # return True if alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True



