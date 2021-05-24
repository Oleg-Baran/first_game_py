# Импорт библиотеки pygame
import pygame

# Инициализируем движок pygame
pygame.init()

# Определяем несколько цветов, которые мы будем
# использовать (RGB)
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

pi = 3.141592653

# Устанавливаем размеры окна
size = [400, 500]
screen = pygame.display.set_mode(size)

# Устанавливаем заголовок окна
pygame.display.set_caption("Крутая игра")

# Цикл работает пока пользователь не закроет окно
done = False
clock = pygame.time.Clock()

while done == False:
 # Следующяя строка ограничивает наш цикл 10 кадрами в секунду.
 # Если этого не сделать, то игра будет использовать
 # максимальное колличество ресурсов.
 clock.tick(10)
 
 for event in pygame.event.get():  # Проходимся по событиям
  if event.type == pygame.QUIT: # Если пользователь закрыл окно
   done = True # Сигнализируем что цикл пора завершать
 
 # Все рислвание происходит после нашего for-цикла,
 # но внутри главного цикла ( while done==False ).
 
 # Очищаем экран
 screen.fill(white)
 font = pygame.font.Font(None, 25)
 text = font.render("My text", True, black)

 pygame.draw.rect(screen, green, [20,20, 250, 100], 2)
 pygame.draw.circle(screen, green, (100, 100), 50)
 screen.blit(text, [50, 50] )
 
 pygame.display.flip()

pygame.quit()