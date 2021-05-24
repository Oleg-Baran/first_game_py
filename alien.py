import pygame
from pygame.sprite import Sprite
from ship import Ship


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position.""" 
        ship = Ship(screen, ai_settings)       
        super(Alien, self).__init__()  
        self.screen = screen    
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('enemy1.1.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = 625
        self.rect.y = 300
        self.hp = 4
        self.move_m = [self.upload_img("enemy1.2.png"), self.upload_img("enemy1.2.png"), self.upload_img("enemy1.3.png")]
        self.i = 0
        self.fps = 7
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self, ship):   
        """Draw the alien at its current location."""
        
        self.image = self.move_m[self.i // self.fps]
        self.i += 1
        if self.i >= len(self.move_m) * self.fps:
            self.i = 0

        self.screen.blit(self.image, self.rect)
        self.rect.x -= 1
        self.rect.y = ship.rect.y - 5
        #self.rect.y = ship.rect.y      
        if self.rect.x == 100:
            #self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x += 525
    def upload_img(self, img):
        return pygame.transform.scale(pygame.image.load(img).convert_alpha(), (75, 75))