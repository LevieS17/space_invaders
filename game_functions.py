# import libraries
import pygame
import sys
from bullets import Bullets
from aliens import Alien
#from settings import Settings


def check_events(settings, screen, ship, bullets):
    #checks for key/mouse events and responds
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key is pressed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event,settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)

# moves the ship left and right and up and down
def keydown_event(event,settings, screen, ship, bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        if event.key == pygame.K_UP:
            ship.moving_up = True
        if event.key == pygame.K_DOWN:
            ship.moving_down = True
        if event.key == pygame.K_SPACE:
            new_bullet = Bullets(settings, screen, ship)
            bullets.add(new_bullet)


# moves the ship up and down
def keyup_event(event, ship):

        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False

def create_fleet(settings, screen, ship, aliens):
    #create a fleet of aliens
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range (number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)


def get_number_of_aliens(settings, alien_width):
    # Determine the number of aliens that fit in a row
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens

def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height -  6 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    # Create alien and place it on a row
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def check_collision(aliens, bullets, settings):
    alien_collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if alien_collision:
        settings.points += 1
        print(settings.points)

def print_text(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Aliens Killed/Points:" + str(0 + settings.points), True, (255, 0, 0))
    screen.blit(surface, (430, 570))

def update_screen(settings, screen, ship, bullets, aliens):
    # color the screen with the background color
    screen.fill(settings.bg_color)

    # update screen
    ship.update()

    # Draw the ship on the screen
    ship.blitme()

    # check collisions and blow up alien if hit by bullet
    check_collision(bullets, aliens, settings)

    # Draw bullets on the screen
    for bullet in bullets.sprites():
        bullet.draw_bullets()
        bullet.update()

    # Draw the fleet of aliens
    aliens.draw(screen)
    aliens.update()
    print_text(settings, screen)

    # update the display
    pygame.display.flip()

