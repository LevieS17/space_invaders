
class Settings():
    # A class to store all settings for alien invasion
    def __init__(self):
        #screen settings
        self.bg_color = (100,100,100)
        self.screen_width = 800
        self.screen_height = 600

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        # player settings
        self.lives = 3
        self.score = 0


