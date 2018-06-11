#!/usr/bin/env python3

'''
@Author Abdul-Razak Adam
This is the entry point to my program
'''
from occupancy_algorithm import GenerateMap


if __name__ == '__main__':
    WIDTH = 3  #width of the grid
    HEIGHT = 3 #height of the grid
    direction = 'N' #starting direction of the robot in relation to the grid
    current_position = (HEIGHT - 1, 0)  #starting position of the robot
    SPEED = 300 #speed of the robot
    CELL_SIZE = 45 #size of a cell

    #create an object of GenerateMap object
    map = GenerateMap(HEIGHT, WIDTH, current_position, direction, SPEED, CELL_SIZE)
    map.createMap() #generate representation of the robot's environment 
