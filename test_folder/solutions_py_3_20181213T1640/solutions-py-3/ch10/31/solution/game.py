## A game similar to Frogger.  The solution to this exercise builds on the
#  solution to Problem 29.  The additions are marked by comments that begin
#  with Problem 31.
import pygame
from random import randint

def main():
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

      # Problem 31: Load the high scores
      self._high_scores = []

      try:
        hs = open("highscores.txt", "r")
        for line in hs:
          parts = line.rstrip().split(",")
          score = int(parts[0])
          init = parts[1]
          self._high_scores.append((score, init))
        hs.close()
      except IOError:
        # Problem 31: Leave the high scores list empty if we failed to read
        # data out of the high scores file.
        pass

      # Problem 31: Game state can be playing (0) or input for a high score (1).
      self._game_state = 0

      # Problem 31: Set up the necessary fonts.
      pygame.font.init()
      self._small_font = pygame.font.SysFont('arial', 20)
      self._big_font = pygame.font.SysFont('arial', 40)

      # Problem 31: Keep track of the information needed for high scores.
      self._current_score = 0
  
   def setScore(self, score) :
      self._current_score = score

   def getScore(self) :
      return self._current_score

   def mouseButtonDown(self, x, y) :
      return
  
   def keyDown(self, key) :
      # Problem 31: Handle key presses when entering initials for a high score.
      if key >= pygame.K_a and key <= pygame.K_z and len(self._initials) < 3 :
         self._initials += chr(key - 32)
      if key == pygame.K_BACKSPACE and self._initials != "" :
         self._initials = self._initials[0 : len(self._initials) - 1]
      if key == pygame.K_RETURN or key == pygame.K_KP_ENTER :
         # Add the current score to the high score list, resort the list
         # and confine it to 10 entries.
         self._high_scores.append((self._current_score, self._initials))
         self._high_scores.sort()
         if len(self._high_scores) > 10 :
            self._high_scores = self._high_scores[0 : 10]

         # Write the new high scores to the highscores file
         hs = open("highscores.txt", "w")
         for (init, score) in self._high_scores :
            hs.write("%s,%s\n" % (init, score))
         hs.close()

         # Restart the game.
         self._current_score = 0
         self._initials = ""
         self._game_state = 0
         self._ticks = 0
         self._game_end_tick = -91
    
   def update(self) :
      self._sprites.update()
    
   def draw(self) :
      self._sprites.draw(self._display)
      if self._game_state == 0 :
         # Problem 31: Draw the high score list.
         textsurface = self._small_font.render("High Scores", True, (0,0,0))
         textrect = textsurface.get_rect(center=(100,20))
         self._display.blit(textsurface, textrect) 

         y = 40
         for (score, init) in self._high_scores :
            textsurface = self._small_font.render("%s - %d" % (init, score), True, (0,0,0))
            textrect = textsurface.get_rect(center=(100,y))
            self._display.blit(textsurface, textrect) 
            y += 20

      else :
         # Problem 31: Display the interface that lets players enter their 
         # initials
         textsurface = self._big_font.render("Enter Your Initials", True, (0,0,0))
         textrect = textsurface.get_rect(center=(400,300))
         self._display.blit(textsurface, textrect) 
         textsurface = self._big_font.render(self._initials, True, (0,0,0))
         textrect = textsurface.get_rect(center=(400,400))
         self._display.blit(textsurface, textrect) 
   
   # Problem 31: End the game with a win
   def win(self, score) :
      self._current_score = score
      self._game_end_tick = self.getTicks()
      self.add(self._won) 
      self._initials = ""

   # Problem 31: End the game with a loss
   def lose(self, score) :
      self._game_end_tick = self.getTicks()
      self.add(self._lost) 

    
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
  
   def keyDown(self, key) :
      if self._alive :
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

class SnakeGame(GameBase) :
   def __init__(self) :
     super().__init__(800, 600)        
     self._snake = Snake(400, 600)
     self._frog = ImageSprite(400, 100, "frog.bmp") 
     self._cars = pygame.sprite.Group()
     self._frog_alive = True     
     self._game_end_tick = -91
     self._won = ImageSprite(300, 400, "won.bmp")
     self._lost = ImageSprite(300, 400, "lost.bmp")

   def addCar(self, lane) :
      if lane == 0 :
         x = -100
      else:
         x = self._width
      newCar = Car(x, lane)
      self._cars.add(newCar)
      self.add(newCar)

   def keyDown(self, key) : 
      super().keyDown(key)
      # Problem 31: Only allow the snake to move when playing the game (not
      # when a high score is being entered).
      if self._game_state == 0 and self.getTicks() >= 480 :
         self._snake.keyDown(key)

   def update(self) :
      super().update()

      # Problem 31: If the game is currently being played (rather than entering
      # a high score).
      if self._game_state == 0 :
         if self.getTicks() % 240 == 0 : # Add a new car to each lane
            self.addCar(0)
            self.addCar(1)              
     
         if self.getTicks() == 480 :
            self._won.kill()
            self._lost.kill()
            self._snake = Snake(400, 600)
            self._frog_alive = True
            self.add(self._snake) 
            self.add(self._frog) 
   
         if self.getTicks() == self._game_end_tick + 90 :
            self._sprites = pygame.sprite.LayeredUpdates()
            self._cars = pygame.sprite.Group()
            self._ticks = -1
            self._game_end_tick = -91
            if self._current_score > 0 and (len(self._high_scores) < 10 or self._current_score < self._high_scores[-1][0]) :
               self._game_state = 1
            
         if pygame.sprite.spritecollideany(self._snake, self._cars) and self._snake._alive :
            self._snake.die()
            self.lose()
            
         if (pygame.sprite.collide_rect(self._snake, self._frog)) and self._frog_alive : 
            self._frog.kill()
            self._frog_alive = False
            self.win(self.getTicks() - 480)

   def draw(self) :
      super().draw()

main()
