# -*- coding: utf-8 -*-

"""Main module."""

class led_tester:
    
    def __init__(self, N):
        self.grid_size = N
        self.grid = [[0 for x in range(self.grid_size)] for y in range(self.grid_size)]
        
    def turn_on(self, start_point1, start_point2, end_point1, end_point2):
        for i in range(start_point1, end_point1+1):
            for j in range (start_point2,end_point2+1):
                self.grid[i][j] = 1
    
    def turn_off(self, start_point1, start_point2, end_point1, end_point2):
        for i in range(start_point1, end_point1+1):
            for j in range (start_point2,end_point2+1):
                self.grid[i][j] = 0
    
    def switch(self, start_point1, start_point2, end_point1, end_point2):
        for i in range(start_point1, end_point1+1):
            for j in range (start_point2,end_point2+1):
                self.grid[i][j] = not self.grid[i][j]
