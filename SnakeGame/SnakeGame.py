#tengo que importar esto ni no, no sabe que estoy ejecutando
import pygame, sys, random
from pygame.math import Vector2
pygame.init()

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

#esto va primero  porque si no lo del logo y ventana no te lo tira
GREEN = (155, 188, 15)
DARK_GREEN = ( 48,98,48)
OFFSET = 75
#este igual, aunque mas que todo este
cell_size = 25
number_of_cells = 25

#aqui hacemos la comida, serpiente y una clase para el juego(snake y food) y ya me da igual que idioma estoy escribiendo
class Food:
  def __init__ (self, snake_body):
     self.position = self.generate_random_pos(snake_body)     

  def draw(self):
     food_rect = pygame.Rect(OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)  
     screen.blit(food_surface,food_rect) 

  def generate_random_cell(self):
     x = random.randint(0, number_of_cells-1)
     y = random.randint(0, number_of_cells -1)
     return Vector2(x,y)

  def generate_random_pos(self, snake_body): 
     position = self.generate_random_cell()
     while position in snake_body:
         position = self.generate_random_cell()
     return position
    
class Snake:
  def __init__(self):
      self.body = [Vector2(6, 9), Vector2(5, 9), Vector2(4, 9)]
      self.direction = Vector2(1, 0)
      self.add_segment = False

  def draw(self):
      for segment in self.body:
          segment_rect = (OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size)
          pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

  def update(self):
      self.body.insert(0, self.body[0] + self.direction)
      if self.add_segment == True:
          self.add_segment = False
      else:
         self.body = self.body[:-1]

  def reset(self):
         self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
         self.direction = Vector2(1,0)

class Game:
   def __init__(self):
      self.snake = Snake()
      self.food = Food(self.snake.body)
      self.state = "RUNNING"
      self.score = 0

   def draw(self):
      self.food.draw()
      self.snake.draw()

   def update(self):
      if self.state == "RUNNING":
            self.snake.update()
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.check_collision_with_tail()

   def check_collision_with_food(self):
      if self.snake.body[0] == self.food.position:
         self.food.position = self.food.generate_random_pos(self.snake.body)
         self.snake.add_segment = True
         self.score += 1

   def check_collision_with_edges(self):
      if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
          self.game_over()
      if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
          self.game_over()

   def game_over(self):
      self.snake.reset()
      self.food.position = self.food.generate_random_pos(self.snake.body)
      self.state = "STOPPED"
      self.score = 0

   def check_collision_with_tail(self):
      headless_body = self.snake.body[1:]
      if self.snake.body[0] in headless_body:
         self.game_over()

# logo and window
# make logo and then window so it can work and 32x32 logo
icon = pygame.image.load("C:\\Proyectos\\Python\\SnakeGame\\Snake-icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((2*OFFSET + cell_size*number_of_cells,2*OFFSET + cell_size*number_of_cells))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
game = Game()
#no encontre una imagen a tamano 32x32 asi que toca formatearla a codigo
food_surface = pygame.image.load("C:\\Proyectos\\Python\\SnakeGame\\food.png").convert_alpha()
food_surface = pygame.transform.scale(food_surface, (cell_size, cell_size))

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 400)

# app loops and quit code
while True:

    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
          game.update()
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

         #busca nsi han apretado cualquier boton incluiudo esc
        if event.type == pygame.KEYDOWN:
          if game.state == "STOPPED":
             game.state = "RUNNING"
          if event.key == pygame.K_UP and game.snake.direction !=  Vector2(0, 1):
            game.snake.direction = Vector2(0, -1)
          if event.key == pygame.K_DOWN and game.snake.direction !=  Vector2(0, -1):
            game.snake.direction = Vector2(0, 1)
          if event.key == pygame.K_LEFT and game.snake.direction !=  Vector2(1, 0):
            game.snake.direction = Vector2(-1, 0)
          if event.key == pygame.K_RIGHT and game.snake.direction !=  Vector2(-1, 0):
            game.snake.direction = Vector2(1, 0)

         
          if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()


    #de aqui se dibuja lo anterior
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN, 
                     (OFFSET-5, OFFSET-5, cell_size*number_of_cells+10, cell_size*number_of_cells+10), 5,)
    game.draw()
    title_surface = title_font.render("RetrO snAKE", False, DARK_GREEN) # yo cambia el aa a falso
    score_surface = score_font.render(str(game.score), False, DARK_GREEN) # yo cambia el aa a falso
    screen.blit(title_surface, (OFFSET-5, 20))
    screen.blit(score_surface, (OFFSET-5, OFFSET + cell_size*number_of_cells +10))
    #aqui se actualiza cada fps por asi decirlo
    pygame.display.update()
    clock.tick(60)

pygame.QUIT()