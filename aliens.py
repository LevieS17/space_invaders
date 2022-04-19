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
        self.image = pygame.transform.scale(self.image, (40,20)) # scales alien ship
        self.rect = self.image.get_rect()

        ##set starting location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.left = self.rect.left
        self.rect.right = self.rect.right
        self.rect.top = self.rect.top

        self.top = float(self.rect.top)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # spacing for the fleet
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

        self.speed = 1
        self.direction = 1

        self.alien_right = True
        self.alien_left = False


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
        elif self.rect.left <= -1:
            return True

    def update(self):
        if self.check_wall():
            self.direction *= -1
            self.rect.y += self.rect.height
            # self.y = self.rect.y
        self.x += self.speed * self.direction
        self.rect.x = self.x
        self.rect.y = self.rect.y




