# import libraries
import pygame
import sys
from bullets import Bullets
from aliens import Alien
#from settings import Settings


def check_events(settings, screen, ship, bullets, play_button):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                settings.game_active = True

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

def check_fleet(aliens,settings):
    if len(aliens) == 0:
        settings.fleet_lim += 1

        return True
    else:
        return False


def game_end(settings):
    if settings.fleet_lim ==3:
        print("your score was " + str(settings.score))
        return True
    elif settings.lives ==0:
        print("Your dead")
        print("your score was " + str(settings.score))
        return True
    else:
        return False

def new_wave(settings, screen, ship, aliens):
    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens)
        settings.wave_number += 1
        settings.alien_speed = settings.wave_number*4

def close_game(settings):
    if game_end(settings) == True:
        sys.exit()



def check_collision(settings, screen, ship, bullets, aliens):
    alien_collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if alien_collision:
        settings.points += 1
        print(settings.points)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, screen, ship, aliens, bullets)

    alien_invasion(settings, screen, ship, aliens, bullets)

def ship_hit(settings, screen, ship, aliens, bullets):
    settings.lives -= 1
    if settings.lives > 0:
        end_game(settings)

def end_game(settings):
    print("Congrats game is over! Point total is ", settings.points)
    settings.game_on = False

def alien_invasion(settings, screen, ship, aliens, bullets):
    for alien in aliens:
        if alien.rect.bottom > settings.screen_height:
            settings.score -= 1

def print_text(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Aliens Killed/Points:" + str(0 + settings.points), True, (255, 0, 0))
    screen.blit(surface, (430, 570))

def update_screen(settings, screen, ship, bullets, aliens, play_button):
    # color the screen with the background color
    screen.fill(settings.bg_color)

    if not settings.game_active:
        play_button.draw_button()

    elif settings.game_active:

        # update screen
        ship.update(settings)

        # Draw the ship on the screen
        ship.blitme()

        # check collisions and blow up alien if hit by bullet
        check_collision(settings, screen, ship, bullets, aliens)

        # Draw bullets on the screen
        for bullet in bullets.sprites():
            bullet.draw_bullets()
            bullet.update()

        # Draw the fleet of aliens
        aliens.draw(screen)
        aliens.update()
        print_text(settings, screen)

        new_wave(settings, screen, ship, aliens)

    # update the display
    pygame.display.flip()

