#!/usr/bin/env python3
'''
@Author : Abdul-Razak Adam
This class generates a 2-D array representation of the environment of the robot. The size of the grid, the current position 
and the direction of the robot in relation to the map is specified. 
    Algorithm
        At each free cell:
            Get the free neighbours of the cell, Priority is given to the left neighbours hence we visit the left neighbour, then 
            the forward then the right neighbours. Update the map with detected obstacles.
            if atleast a neighbour is free, and it is not visited, move to neighbouring cell and update the map. 
            if not neighbour, then backtrack
            if after backtracking an no neighbour then end.

'''
from cell import Cell
from robot import Robot
import time


'''
height :: height of the grid
width :: width of the grid
start_position :: start position eg (2,0)
start_direction ::starting direction of the robot eg 'N', 'E', 'S' or 'W'
speed :: speed of movement of the robot
 cell_size :: size of the size in cm
'''
class GenerateMap(object):
    def __init__(self, height, width, start_position, start_direction, speed, cell_size):
        self.WIDTH = width
        self.HEIGHT = height
        self.direction = start_direction
        self.current_position = start_position
        self.SPEED = speed
        self.CELL_SIZE = cell_size
        self.generate_map()
        #cretae  a robot with motors in port B and C and sensors in 4,3 and 2
        self.robot = Robot('B', 'C', '4','3','2')


    #generate a map with cell
    def generate_map(self):
        self.map = [[0 for x in range(self.WIDTH)] for y in range(self.HEIGHT)]
        for i in range(self.HEIGHT):
            for r in range(self.WIDTH):
                self.map[i][r] = Cell(i, r)
    

    #This method get the average readings of a specified sensor catering for errors 
    def readUSsensorValues(self, sensor):
        d1 = self.robot.getSensorReading(sensor)
        time.sleep(0.1)
        d2 = self.robot.getSensorReading(sensor)
        time.sleep(0.1)
        d3 = self.robot.getSensorReading(sensor)
        time.sleep(0.1)
        ave = (d1 + d2 + d3) / 3
        return ave <= (self.CELL_SIZE - 10)

    
    #Update obstacles in the map as they are encountered from a cell with the robot facing a certain direction
    def mark_obstacles(self, cell, dir):
        h = cell[0]
        w = cell[1]

        if dir == 'N':
            if self.readUSsensorValues('front') and (h - 1) >= 0:
                self.map[h - 1][w].empty = False
            if self.readUSsensorValues('right') and (w + 1) < self.WIDTH:
                self.map[h][w + 1].empty = False
            if self.readUSsensorValues('left') and (w - 1) >= 0:
                self.map[h][w - 1].empty = False
        elif dir == 'E':
            if self.readUSsensorValues('front') and (w + 1) < self.WIDTH:
                self.map[h][w + 1].empty = False
            if self.readUSsensorValues('right') and (h + 1) < self.HEIGHT:
                self.map[h + 1][w].empty = False
            if self.readUSsensorValues('left') and (h - 1) >= 0:
                self.map[h - 1][w].empty = False
        elif dir == 'S':
            if self.readUSsensorValues('front') and (h + 1) < self.HEIGHT:
                self.map[h + 1][w].empty = False
            if self.readUSsensorValues('right') and (w - 1) >= 0:
                self.map[h][w - 1].empty = False
            if self.readUSsensorValues('left') and (w + 1) < self.WIDTH:
                self.map[h][w + 1].empty = False

        elif dir == 'W':
            if self.readUSsensorValues('front') and (w - 1) >= 0:
                self.map[h][w - 1].empty = False
            if self.readUSsensorValues('right') and (h - 1) >= 0:
                self.map[h - 1][w].empty = False
            if self.readUSsensorValues('left') and (h + 1) < self.HEIGHT:
                self.map[h + 1][w].empty = False

    #for a given cell and direction, this method returns all the free neigbours/ cell that are not visited
    def getNeighborCells(self, cell, dir):
        h = cell[0]
        w = cell[1]

        neigbours = []

        if dir == 'N':
            if (((h - 1) >= 0) and (not self.readUSsensorValues('front'))):
                if (not self.map[h - 1][w].sensed):
                    neigbours.append((h - 1, w, 'N'))

            if(((w + 1) < self.WIDTH) and (not self.readUSsensorValues('right'))):
                if (not self.map[h][w + 1].sensed):
                    neigbours.append((h, w + 1, 'E'))

            if(((w - 1) >= 0) and (not self.readUSsensorValues('left'))):
                if (not self.map[h][w - 1].sensed):
                    neigbours.append((h, w - 1, 'W'))

        elif dir == 'E':
            if (((w + 1) < self.WIDTH) and (not self.readUSsensorValues('front'))):
                if (not self.map[h][w + 1].sensed):
                    neigbours.append((h, w + 1, 'E'))

            if(((h + 1) < self.HEIGHT) and (not self.readUSsensorValues('right'))):
                if (not self.map[h + 1][w].sensed):
                    neigbours.append((h + 1, w, 'S'))

            if(((h - 1) >= 0) and (not self.readUSsensorValues('left'))):
                if (not self.map[h - 1][w].sensed):
                    neigbours.append((h - 1, w, 'N'))

        elif dir == 'S':
            if (((h + 1) < self.HEIGHT) and (not self.readUSsensorValues('front'))):
                if (not self.map[h + 1][w].sensed):
                    neigbours.append((h + 1, w, 'S'))

            if(((w - 1) >= 0) and (not self.readUSsensorValues('right'))):
                if (not self.map[h][w - 1].sensed):
                    neigbours.append((h, w - 1, 'W'))

            if(((w + 1) < self.WIDTH) and (not self.readUSsensorValues('left'))):
                if (not self.map[h][w + 1].sensed):
                    neigbours.append((h, w + 1, 'E'))

        elif dir == 'W':
            if(((w - 1) >= 0) and (not self.readUSsensorValues('front'))):
                if (not self.map[h][w - 1].sensed):
                    neigbours.append((h, w - 1, 'W'))

            if (((h - 1) >= 0) and (not self.readUSsensorValues('right'))):
                if (not self.map[h - 1][w].sensed):
                    neigbours.append((h - 1, w, 'N'))

            if(((h + 1) < self.HEIGHT) and (not self.readUSsensorValues('left'))):
                if (not self.map[h + 1][w].sensed):
                    neigbours.append((h + 1, w, 'S'))

        return neigbours

    #this method prints the representation of the map of the robot with 
    #   'FREE' for free cell
    #   'NOOO' for occupied cell
    def print_map(self):
        for i in range(self.HEIGHT):
            for f in range(self.WIDTH):
                free = self.map[i][f].empty
                if free:
                    print('FREE', end=' | ')  # if free
                else:
                    print('NOOO', end=' | ')  #if occupied
            print()


    #This method marks a cell as visited/sensed
    def markCellSensed(self, cell):
        self.map[cell[0]][cell[1]].sensed = True

    #display the map indicating visited an unvisited cells
    def sensed_map(self):
        for i in range(self.HEIGHT):
            for r in range(self.WIDTH):
                sensed = self.map[i][r].sensed
                if sensed:
                    print("SENSED", end=' | ')
                else:
                    print("NOOOON", end=' | ')
            print()

    '''
    This function check the position and direction of the robot, compute it neighbours and make the necessary movement required
    '''
    def move(self, current_dir, goto_direction):
        if (current_dir == 'N'):
            if goto_direction == 'N':
                #go straight
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
            elif goto_direction == 'E':
                #turn right
                self.robot.turnRight(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'E'
            elif goto_direction == 'W':
                #turn left
                self.robot.turnLeft(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'W'
        elif current_dir == 'E':
            if goto_direction == 'E':
                #go straight
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)

            elif goto_direction == 'S':
                #turn right
                self.robot.turnRight(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'S'
            elif goto_direction == 'N':
                #turn left
                self.robot.turnLeft(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'N'
        elif current_dir == 'S':
            if goto_direction == 'S':
                #go straight
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
            elif goto_direction == 'W':
                #turn right
                self.robot.turnRight(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'W'
            elif goto_direction == 'E':
                #turn left
                self.robot.turnLeft(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'E'
        elif current_dir == 'W':
            if goto_direction == 'W':
                #go straight
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
            elif goto_direction == 'N':
                #turn right
                self.robot.turnRight(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'N'
            elif goto_direction == 'S':
                #turn left
                self.robot.turnLeft(9.5, self.SPEED)
                self.robot.moveStraight(self.CELL_SIZE, self.SPEED)
                self.direction = 'S'
    
    #This methods generates and draw the representation by the robot
    def createMap(self):
        start_cell = self.current_position
        while (not self.robot.TOUCH_SENSOR.value()):
            self.markCellSensed(self.current_position)
            self.mark_obstacles(self.current_position, self.direction)
            neighbours = self.getNeighborCells(self.current_position, self.direction)
            if (len(neighbours) > 0):
                neighbour = neighbours[0]
                #move & update cell
                cell = (neighbour[0], neighbour[1])
                dir = neighbour[2]

                #move
                self.move(self.direction, dir)
                time.sleep(2)
                self.markCellSensed(cell)
                self.current_position = cell
            else:
                print('Backtrack')
                backtrack = False
                h = self.current_position[0]
                w = self.current_position[1]
                if (self.direction == 'N'):
                    if (h + 1) < self.HEIGHT:
                        temp = (h + 1, w)
                        dir = 'S'
                        backtrack = True
                elif(self.direction == 'E'):
                    if (w - 1) >= 0:
                        temp = (h, w - 1)
                        backtrack = True
                        dir = 'W'
                elif (self.direction == 'S'):
                    if (h - 1) >= 0:
                        temp = (h - 1, w)
                        backtrack = True
                        dir = 'N'
                elif (self.direction == 'W'):
                    if (w + 1) < self.WIDTH:
                        temp = (h, w + 1)
                        backtrack = True
                        dir = 'E'
                if backtrack and self.map[temp[0]][temp[1]].empty:
                    self.robot.moveBackward(self.CELL_SIZE, self.SPEED)
                    #turnRight(19.2, SPEED) #turn 180
                    #moveStraight(CELL_SIZE, SPEED)
                    self.current_position = temp
                    #direction = dir
                    time.sleep(2)
                else:
                    print('Thank you')
                    break
            print('....................')
            print('....................')
            self.print_map()
            #sensed_map()
            print("Current Position " + str(self.current_position))
            time.sleep(1)

    
