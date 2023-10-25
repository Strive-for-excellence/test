import pygame
import sys
import tkinter as tk
from snake import Snake
from food import Food
from menu import Menu
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a snake and a food
snake = Snake(WIDTH, HEIGHT)
food = Food(WIDTH, HEIGHT)

# Create a menu
menu = Menu()

# Create a score
score = 0

# Initialize game_started
game_started = False

# Draw the menu before the game starts
if not game_started:
    menu.draw(WIN)

def reset_game():
    global score, snake, food
    score = 0
    snake = Snake(WIDTH, HEIGHT)
    food = Food(WIDTH, HEIGHT)

def game_over():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Game Over", f"Your final score is: {score}")
    root.destroy()
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
            elif event.key == pygame.K_SPACE:  # Add this line to start the game when space is pressed
                game_started = True

    if game_started:  # Add this line to update the game state only when the game has started
        # Update the snake's position
        snake.update()

        # Draw the snake and food
        snake.draw(WIN)
        food.draw(WIN)

        # Check if the snake has eaten the food
        if snake.body[0] == food.position:
            score += 1
            food = Food(WIDTH, HEIGHT)

        # Check if the snake has collided with itself or the game boundary
        if snake.body[0] in snake.body[1:] or snake.body[0][0] < 0 or snake.body[0][0] > WIDTH or snake.body[0][1] < 0 or snake.body[0][1] > HEIGHT:
            game_over()

        # Adjust the speed of the snake and the frequency of food appearance based on the selected difficulty level
        if menu.difficulty == 'Easy':
            FPS = 30  # Reduced from 60 to 30
        elif menu.difficulty == 'Medium':
            FPS = 60  # Reduced from 90 to 60
        elif menu.difficulty == 'Hard':
            FPS = 90  # Reduced from 120 to 90

    pygame.display.update()