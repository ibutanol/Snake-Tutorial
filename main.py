import pygame
from pygame.locals import *
import time

blocksize = 40
class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = blocksize * 3
        self.y = blocksize * 3
    def draw_apple(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()

class Snake:
    def __init__(self,surface, length):
        self.length = length
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [blocksize]*length    
        self.y = [blocksize]*length
        self.direction = 'down'
    
    def draw(self):
        self.parent_screen.fill((44,34,34))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_down(self):
        self.direction = 'down'
    def move_up(self):
        self.direction = 'up'

    def walk(self):
        for i in range(self.length -1,0,-1):
            self.x[i] = self.x[i -1]
            self.y[i] = self.y[i -1]
        if self.direction == 'left':
            self.x[0] -= blocksize
        if self.direction == 'right':
            self.x[0] += blocksize
        if self.direction == 'up':
            self.y[0] -= blocksize
        if self.direction == 'down':
            self.y[0] += blocksize
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((44,34,34))
        self.snake = Snake(self.surface, 10)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw_apple()
    
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and y1 <= y2 + blocksize:
            return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw_apple()


    def run (self):
        running = True

        while running: 
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                            running = False 
    
                    if event.key == K_UP:
                        self.snake.move_up()
                        
                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_LEFT:
                        self.snake.move_left()
                     
                elif event.type == QUIT: 
                        running = False 

            self.play()
            time.sleep(0.2)

if __name__ == '__main__':
    game = Game()
    game.run()

#weitere Idee: SchlangenKopf wird draw() offen wenn es ein apfel frisst und draw() zurueck wenn esfertig is
