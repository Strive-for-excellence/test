   import pygame
   import sys

   # Initialize Pygame
   pygame.init()

   # Set up some constants
   WIDTH, HEIGHT = 800, 600
   FPS = 60

   # Create the game window
   WIN = pygame.display.set_mode((WIDTH, HEIGHT))

   # Main game loop
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()