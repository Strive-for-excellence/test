   import pygame

   class Snake:
       def __init__(self):
           self.size = 10
           self.color = (0, 255, 0)
           self.direction = 'UP'
           self.body = [(WIDTH // 2, HEIGHT // 2)]