
class Settings():
    # A class to store all settings for alien invasion
    def __init__(self):
        #screen settings
        self.bg_color = (100,100,100)
        self.screen_width = 800
        self.screen_height = 600

        # bullet settings
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # alien settings
        self.alien_speed = 10

        # ship speed
        self.ship_speed = 7

        # wave settings
        self.wave_number = 1

        # Difficulty Settings
        self.difficulty_scale = float(1+ self.wave_number*5)

        # player settings
        self.lives = 3
        self.points = 0

        # play game
        self.game_active = False


