import pygame
import sys
from snake import Snake
from food import Food
from menu import Menu
from pygame import messagebox

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a snake and a food
snake = Snake()
food = Food()

# Create a menu
menu = Menu()

# Create a score
score = 0

def reset_game():
    global score
    score = 0
    snake = Snake()
    food = Food()

def game_over():
    messagebox.showinfo("Game Over", f"Your final score is: {score}")
    reset_game()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = 'UP'
            elif event.key == pygame.K_DOWN:
                snake.direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                snake.direction = 'RIGHT'
            elif event.key == pygame.K_1:
                menu.change_difficulty('Easy')
            elif event.key == pygame.K_2:
                menu.change_difficulty('Medium')
            elif event.key == pygame.K_3:
                menu.change_difficulty('Hard')

    # Draw the menu before the game starts
    if not game_started:
        menu.draw(WIN)

    # Handle user inputs
    # Update game state
    # Render game objects

    # Check if the snake has eaten the food
    if snake.body[0] == food.position:
        score += 1
        food = Food()

    # Check if the snake has collided with itself or the game boundary
    if snake.body[0] in snake.body[1:] or snake.body[0][0] < 0 or snake.body[0][0] > WIDTH or snake.body[0][1] < 0 or snake.body[0][1] > HEIGHT:
        game_over()

    # Adjust the speed of the snake and the frequency of food appearance based on the selected difficulty level
    if menu.difficulty == 'Easy':
        FPS = 60
    elif menu.difficulty == 'Medium':
        FPS = 90
    elif menu.difficulty == 'Hard':
        FPS = 120

    pygame.display.update()