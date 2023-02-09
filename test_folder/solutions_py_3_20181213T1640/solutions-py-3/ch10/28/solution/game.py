## A game similar to Frogger.  Most of the code for this game is provided
#  in Toolbox 10.1.  The additions beyond what is shown in that toolbox
#  are marked by comments that begin with Problem 28.
import pygame
from random import randint

def main() :
   game = SnakeGame()
   game.run()

class ImageSprite(pygame.sprite.Sprite) :
   def __init__(self, x, y, filename) :
      super().__init__()
      self.loadImage(x, y, filename)
  
   def loadImage(self, x, y, filename) :
      img = pygame.image.load(filename).convert()
      MAGENTA = (255, 0, 255)
      img.set_colorkey(MAGENTA)
      self.image = img
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y - self.rect.height
     
   def moveBy(self, dx, dy) :
      self.rect.x = self.rect.x + dx
      self.rect.y = self.rect.y + dy

class Car(ImageSprite) :
   def __init__(self, x, lane) :
      self._lane = lane
      y = 300 + 200 * lane        
      super().__init__(x, y, "car" + str(randint(0, 9)) + ".bmp") 
     
      if lane == 0 :
         self.image = pygame.transform.flip(self.image, True, False)
      self._layer = 1

   def update(self) :
      if self._lane == 0 : 
         self.rect.x = self.rect.x + 1
      else :
         self.rect.x = self.rect.x - 1

class GameBase:
   def __init__(self, width, height) :
      pygame.init()
      self._width = width
      self._height = height
  
      self._display = pygame.display.set_mode((self._width, self._height))
      self._clock = pygame.time.Clock()
      self._framesPerSecond = 30
      self._sprites = pygame.sprite.LayeredUpdates()
      self._ticks = 0
      pygame.key.set_repeat(1, 120)
  
   def mouseButtonDown(self, x, y) :
      return
  
   def keyDown(self, key) :
      return
    
   def update(self) :
      self._sprites.update()
    
   def draw(self) :
      self._sprites.draw(self._display)
    
   def add(self, sprite) :
      self._sprites.add(sprite)
        
   def getTicks(self) :
      return self._ticks
        
   def quit(self) :
      pygame.quit()        
    
   def run(self) :
      while True :
         for event in pygame.event.get() :
            if event.type == pygame.QUIT :
               self.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN :                    
               self.mouseButtonDown(event.pos[0], event.pos[1])
            elif event.type == pygame.KEYDOWN :
               self.keyDown(event.key)
                    
         self.update()
         WHITE = (255, 255, 255)
         self._display.fill(WHITE)
         self.draw()
         pygame.display.update()
         self._clock.tick(self._framesPerSecond)
         self._ticks = self._ticks + 1

class Snake(ImageSprite) :
   def __init__(self, x, y) :
         super().__init__(x, y, "snake.bmp") 
         self._alive = True
         self._layer = 2
         # Problem 28: Add a data member that keeps track of whether or not
         #             the snake has won the game.
         self._won = False
  
   def keyDown(self, key) :
      # Problem 28: Add the constraint that the snake has not won to the if
      #             statement condition.
      if self._alive and not self._won :
         distance = 20
         if key == pygame.K_w or key == pygame.K_UP :
            self.moveBy(0, -distance)
         elif key == pygame.K_a  or key == pygame.K_LEFT :
            self.moveBy(-distance, 0)
         elif key == pygame.K_s  or key == pygame.K_DOWN :
            self.moveBy(0, distance)
         elif key == pygame.K_d  or key == pygame.K_RIGHT :
            self.moveBy(distance, 0)
         
   def die(self) :
      if self._alive :
         self.image = pygame.transform.flip(self.image, True, True)
         self._alive = False

   # Problem 28: Add a method that marks that the snake has won the game.
   def win(self) :
     self._won = True

class SnakeGame(GameBase) :
   def __init__(self) :
     super().__init__(800, 600)        
     self._snake = Snake(400, 600) 
     self._frog = ImageSprite(400, 100, "frog.bmp") 
     self._cars = pygame.sprite.Group()
     # Problem 28: Load the crown that will be placed on the snake's head 
     #             when it wins.
     self._crown = ImageSprite(400, 100, "crown.bmp")

   def addCar(self, lane) :
      if lane == 0 :
         x = -100
      else :
         x = self._width
      newCar = Car(x, lane)
      self._cars.add(newCar)
      self.add(newCar)

   def keyDown(self, key) : 
      self._snake.keyDown(key)

   def update(self) :
      super().update()
  
      if self.getTicks() % 240 == 0 : # Add a new car to each lane
         self.addCar(0)
         self.addCar(1)              
  
      if self.getTicks() == 480 :
         self.add(self._snake) 
         self.add(self._frog) 
         
      if pygame.sprite.spritecollideany(self._snake, self._cars) :
         self._snake.die()
         
      if (pygame.sprite.collide_rect(self._snake, self._frog)) : 
         self._frog.kill()
         # Problem 28: Put snake into its win state and draw the crown.
         self._snake.win()
         self.add(self._crown)

main()
