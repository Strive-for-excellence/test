import pygame

class Snake:
    def __init__(self):
        self.size = 10
        self.color = (0, 255, 0)
        self.direction = 'UP'
        self.body = [(WIDTH // 2, HEIGHT // 2)]

    def draw(self, WIN):
        for part in self.body:
            pygame.draw.rect(WIN, self.color, (part[0], part[1], self.size, self.size))

    def update(self):
        if self.direction == 'UP':
            self.body.insert(0, (self.body[0][0], self.body[0][1] - self.size))
        elif self.direction == 'DOWN':
            self.body.insert(0, (self.body[0][0], self.body[0][1] + self.size))
        elif self.direction == 'LEFT':
            self.body.insert(0, (self.body[0][0] - self.size, self.body[0][1]))
        elif self.direction == 'RIGHT':
            self.body.insert(0, (self.body[0][0] + self.size, self.body[0][1]))

        self.body.pop()