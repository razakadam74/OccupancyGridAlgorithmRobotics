#!/usr/bin/env python3

'''
@Author : Abdul-Razak Adam
This class represent a cell in the grid map of the robot.It has several properties including
    - height and width :integers  for locating it position in the grid such as grid[height][width]
    - empty : boolean indicates if the cell is free or contains an obstacle
    - sensed : indicates if a cell is visited by the robot
'''
class Cell(object):

    '''
        Position of cell in grid is [height][width]
    '''
    def __init__(self, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        self.empty = True
        self.sensed = False

    '''
    ToString method for printing the detail of a cell
    '''
    def __str__(self):
        return 'cell ' + str(self.HEIGHT) + ' ' + str(self.WIDTH) + ' IsEmpty :' + str(self.empty) + ' isSensed :' + str(self.sensed)
