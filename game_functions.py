import sys
import pygame
from bullet import Bullet
from alien import Alien
from ship import Ship
from tkinter import *
from tkinter import messagebox

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    #Watch for keyboard and mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ai_settings, screen, ship)

#Events KEYDOWN & KEYUP
def check_events_keydown(event, ai_settings, screen, ship, bullets):
    #Move to right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    #Move to left
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #Move to up
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    #Move to down
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #Fire bullets
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # Closed game
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_events_keyup(event, ai_settings, screen, ship):
    #Stop move to right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    #Stop move to left    
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    #Stop move to up
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    #Stop move to down
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False   

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    #Set bg color
    bg_color = pygame.image.load("bg1.jpg")   
    bg_color = pygame.transform.scale(bg_color, (ai_settings.screen_width, ai_settings.screen_height))
    #Redraw the screen during each pass througt the loop
    screen.blit(bg_color, (0, 0))
    ship.blitme()
    for alien in aliens:
        if ai_settings.ac < 3:
            alien.blitme(ship)
        if pygame.sprite.spritecollideany(alien, bullets):
            alien.hp -= 1
            if alien.hp == 0:
                aliens.remove(alien)
                alien = Alien(ai_settings, screen)
                aliens.add(alien)
                ai_settings.ac +=1
            if ai_settings.ac == 3:
                Tk().wm_withdraw()
                messagebox.showinfo("", "Wou are winner! \n congratulation!!!")
    if ship.rect.x + 20 == alien.rect.left:
        alien.rect.x += 45        
        ship.hp -= 1
        if ship.hp == 0:
            check(ship, alien)
            
    #Make the most recently drawn screen visible
    for bullet in bullets.sprites():
        bullet.draw_bullet()   
        if bullet.rect.x > 700 or bullet.rect.x < 0:
            bullets.remove(bullet)

    pygame.sprite.groupcollide(aliens, bullets, False, True)
    #pygame.sprite.groupcollide(ship, aliens, False, True)
    pygame.display.flip() 

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions. 
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():       
        if bullet.rect.bottom <= 0:   
            bullets.remove(bullet)
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""  
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)   
        new_bullet.direction = ship.direction     
        bullets.add(new_bullet)

def check(ship, alien):
    Tk().wm_withdraw()
    answer = messagebox.askyesno("Game Over!", "Want to play again?")
    if answer == True:
        ship.hp = 4
        ship.rect.x = 150
        alien.rect.x = 625
    elif answer == False:
        sys.exit()

