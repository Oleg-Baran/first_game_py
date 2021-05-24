class Settings():    
    """A class to store all settings for Alien Invasion."""

    def __init__(self): 
        """Initialize the game's settings."""    
        # Screen settings  
        self.screen_width = 800
        self.screen_height = 600

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 2
        self.bullet_color = 0, 0, 60 
        self.bullets_allowed = 3

        #direction
        self.direction = 1
        self.ac = 0 #aliens counter
        
