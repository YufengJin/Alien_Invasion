class Settings():
    """store all classes we used in alien invasion"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51,153,255)
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250,250,250

        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

