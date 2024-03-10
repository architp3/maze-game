import pygame as pg
from queue import PriorityQueue
import math
import random

WIDTH = 800
WIN = pg.display.pygame.display.set_mode((WIDTH, WIDTH))
pg.display.set_caption('Pathfinding Algorithms')

colors = {
    'RED': (255,0,0),
    'GREEN': (0,255,0),
    'BLUE': (0,0,255),
    'GREY': (128,128,128),
    'TURQUOISE': (64,224,208),
    'WHITE': (255,255,255),
    'BLACK': (0,0,0),
    'PURPLE': (160,32,240)
}

class Square:
    def __init__(self, r, c, w, total_rows):
        self.r = r
        self.c = c
        self.x = r * w
        self.y = c * w
        self.color = colors['WHITE']
        self.neighbors = []
        self.w = w
        self.total_rows = total_rows

    def pos(self):
        return self.r, self.c
    
    def is_closed(self):
        return self.color == colors['RED']
    
    def is_open(self):
        return self.color == colors['BLUE']
    
    def is_wall(self):
        return self.color == colors['BLACK']
    
    def is_start(self):
        return self.color == colors['GREEN']
    
    def is_end(self):
        return self.color == colors['PURPLE']
    
    def make_closed(self):
        self.color = colors.RED
    
    def make_open(self):
        self.color = colors.BLUE
    
    def make_wall(self):
        self.color = colors['BLACK']
    
    def make_path(self):
        self.color = colors['PURPLE']
    
    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x,self.y, self.w, self.w))
    
    def change_status(self, grid):
        pass

    def __lt__(self):
        return False


def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2) 

def make_maze(dim, width):
    grid = []
    gap = width//dim

    for i in range(dim):
        grid.append([])
        for j in range(dim):
            grid.append(Square(i,j,gap,dim))

    return grid


def draw_grid(win, dim, width):
    size = width//dim
    for i in range(dim):
        pg.draw.line(win, GREY, (0,i * gap), (width, i * gap))
        for j in range(dim):
            pg.draw.line(win, color['BLACK'], (0,i*size), (width,i*size))