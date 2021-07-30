import pygame
import time
import random
import numpy as np
import os
import tkinter as tk
from tkinter import*

#requirments
'''
pip install pygame
pip install numpy
pip install tkinter
'''
#commands
#"Esc" to close the window

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 600,1500
size = (width, height)

pygame.init()
pygame.display.set_caption("vinay jakkena's grid")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 20
offset = 2


class Grid:
    def _init_(self, rows, columns, scale, offset):
        self.scale = scale
        #cell columns and rows randomly placing by using height and width
        self.columns = int(columns)
        self.rows = int(rows)

        #grid size
        self.size = (self.rows, self.columns)
        
        #numpy ndarray gives inter connection to one end to another end like rubic shape
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        #random number from 0,1 is assigned to the grid
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours( x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next      

    #used for finding the neighbours of the specific cell
    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

    #used for updating the existing grid
    def update_grid_size(self, newx, newy):
        #cell columns and rows randomly placing by using height and width
        self.columns = int(newy)
        self.rows = int(newx)

        #grid size
        self.size = (self.rows, self.columns)
        
        #numpy ndarray gives inter connection to one end to another end like rubic shape
        self.grid_array = np.ndarray(shape=(self.size))

    #used for updating the existing grid values
    def update_random2d_array(self, gridArchieve, gridSize):
        count = 0
        for x in range(self.rows):
            for y in range(self.columns):
                if(count < gridSize):
                    self.grid_array[x][y] = gridArchieve[count]
                    count = count + 1
                else:
                    self.grid_array[x][y] = random.randint(0,1)
                    
# grid is initializing the grid with rows 20 and columns 25
grid = Grid(20,25, scaler, offset)
grid.random2d_array()
grid.Conway(off_color=white, on_color=blue1, surface=screen)
screen.fill(black)
pygame.display.update()

run = True
while run:
    # input value from UI is assigned to inputval
     inputval = 20
     #2d array is converted to 1d array and preserved
     gridArchieve = grid.grid_array.flatten()
     oldGridsize = (grid.rows * grid.columns)
     newGridsize = oldGridsize + inputval
     newRowSize = grid.rows
     newColumnize = grid.columns + inputval/20
     # grid size is updated with the new cells count
     grid.update_grid_size(newRowSize, newColumnize)
     grid.update_random2d_array(gridArchieve, oldGridsize)
     screen.fill(black)
     # grid.Conway is used for applying our logic
     grid.Conway(off_color=white, on_color=blue1, surface=screen)
     pygame.display.update()
     
pygame.quit()
