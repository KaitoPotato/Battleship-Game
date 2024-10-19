import main
import pygame

class Player:
    def __init__(self, name, grid_size):
        self.name = name
        self.grid = self.createGrid(grid_size)
        self.hidden_grid = self.createGrid(grid_size)
        self.points = 0

        self.shield = False
        self.mirror = False

    def createGrid(self, size):
        return [["-" for i in range(size)] for j in range(size)]
    
    def createGrid_(self, size):
        tilemap = [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0 ,0 ,0 ,0 ,0],
                    [0 ,0 ,0 ,0 ,0],
                ]
        return tilemap

    def reveal_square(self, x, y):

        # TODO: Reveal square in pygames

        squareValue = self.grid[x][y]

        return squareValue