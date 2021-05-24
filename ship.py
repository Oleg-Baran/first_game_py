import pygame
from settings import Settings


class Ship():
    def __init__(self, screen, settings):
        x = 150
        y = 350
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.ai_settings = settings
        """Initialize the ship and set its starting position."""
        self.screen = screen
        
        # Load the ship image and get its rect.          
        self.image = pygame.image.load('p0.png')
        self.image = pygame.transform.scale(self.image, (75, 75))     
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_rect = screen.get_rect()
        self.i = 0
        self.fps = 15
        self.move_p = [self.load_img("p0.png"), self.load_img("p1.png")]
        self.hp = 4
        #Icon for game
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)
        self.direction = 1
        

    def blitme(self):
        """Draw the ship at its current location."""
        if self.i >= len(self.move_p) * self.fps:
            self.i = 0

        self.image = self.move_p[self.i // self.fps]
        if self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)


                
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < 740:
            self.rect.x +=2
            self.i += 1
            self.direction = 1
            #for change image!!!
        if self.moving_left and self.rect.left > 40:
            self.rect.x -=2
            self.i += 1
            self.direction = -1
        if self.moving_up and self.rect.top > 325:
            self.rect.y -=2
            self.i += 1
        if self.moving_down and self.rect.bottom < 445:
            self.rect.y +=2
            self.i += 1
            #for change image!!!

    def load_img(self, img):
        return pygame.transform.scale(pygame.image.load(img).convert_alpha(), (75, 75))
        
        
