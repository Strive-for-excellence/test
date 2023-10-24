   import pygame
   import random

   class Food:
       def __init__(self):
           self.size = 10
           self.color = (255, 0, 0)
           self.position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))