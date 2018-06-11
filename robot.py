#!/usr/bin/env python3

'''
@Author : Abdul-Razak Adam
This class--Robot-- contains all the properties and methods that can be perform on the robot. 
It defines the ports sensors and motors are connected to. It also contain several actions that can be performs by the robot include
    -moveStraight(distance, speed) : Move the robot straight for a particular distance at a centain speed
    -moveBackward(distance, speed):Move the robot backward for a particular distance at a centain speed
    -turnRight(distance, speed):turn the robot right for a particular distance at a centain speed
    -turnLeft(distance, speed):turn the robot left for a particular distance at a centain speed
    -stopMotor():Stop the robot
    -getSensorReading(sensor):get the reading of a particular ultrasonic sensor base on the 'left','front' and 'right'

Properties of Robot object
    leftMotor : Left motor
    rightMotor : Right motor
    FRONT_US_SENSOR : UltrasonicSensor infront
    RIGHT_US_SENSOR : UltrasonicSensor to the right
    LEFT_US_SENSOR : UltrasonicSensor to the left
    TOUCH_SENSOR : Touch sensor

'''

from ev3dev.ev3 import LargeMotor, UltrasonicSensor, TouchSensor

class Robot(object):

    BASE = 12.3  #base of the tire
    RADUIS = 3   #radius of the tire
    CIRCUMFERENCE = 17.2 #circumference of the tires


    '''
    left_motor_port :: left motor port
    right_motor_port :: right motor port
    front_us_port :: front ultrasonic sensor port
    right_us_port ::right ultrasonic sensor port
    left_us_port ::left ultrasonic sensor port
    '''
    def __init__(self, left_motor_port, right_motor_port, front_us_port, right_us_port, left_us_port):
        self.leftMotor = LargeMotor('out' + left_motor_port)
        self.rightMotor = LargeMotor('out' + right_motor_port)
        self.FRONT_US_SENSOR = UltrasonicSensor('in'+front_us_port)
        self.RIGHT_US_SENSOR = UltrasonicSensor('in'+right_us_port)
        self.LEFT_US_SENSOR = UltrasonicSensor('in'+left_us_port)
        self.TOUCH_SENSOR = TouchSensor()

        assert self.leftMotor.connected, "Connect left Motor to port" + \
            str(left_motor_port)
        assert self.rightMotor.connected, "Connect right Motor to port" + \
            str(right_motor_port)
        assert self.TOUCH_SENSOR.connected, "Connect a touch sensor"
        assert self.FRONT_US_SENSOR.connected, "Connect the ultrasound sensor in the front"
        assert self.RIGHT_US_SENSOR.connected, "Connect the ultrasound sensor on the right"
        assert self.LEFT_US_SENSOR.connected, "Connect the ultrasound sensor on the left"

        #set sensor mode to cm
        self.FRONT_US_SENSOR.mode = 'US-DIST-CM'
        self.RIGHT_US_SENSOR.mode = 'US-DIST-CM'
        self.LEFT_US_SENSOR.mode = 'US-DIST-CM'
    

    #move straight
    def moveStraight(self, distance, speed):
        n = (360 * distance) / self.CIRCUMFERENCE
        self.rightMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.leftMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.rightMotor.wait_while('running')
        self.leftMotor.wait_while('running')

    #move backward
    def moveBackward(self, distance, speed):
        n = (360 * distance) / self.CIRCUMFERENCE
        n = (-1 * n)
        self.rightMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.leftMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.rightMotor.wait_while('running')
        self.leftMotor.wait_while('running')

    #left left
    def turnLeft(self, distance, speed):
        n = (360 * distance) / self.CIRCUMFERENCE
        m = (-1 * n)
        self.rightMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.leftMotor.run_to_rel_pos(
            position_sp=m, speed_sp=speed, stop_action="brake")
        self.rightMotor.wait_while('running')
        self.leftMotor.wait_while('running')

    #turn right
    def turnRight(self, distance, speed):
        n = (360 * distance) / self.CIRCUMFERENCE
        m = (-1 * n)
        self.rightMotor.run_to_rel_pos(
            position_sp=m, speed_sp=speed, stop_action="brake")
        self.leftMotor.run_to_rel_pos(
            position_sp=n, speed_sp=speed, stop_action="brake")
        self.rightMotor.wait_while('running')
        self.leftMotor.wait_while('running')

    #stop robot movement
    def stopMotor(self):
        self.rightMotor.stop()
        self.leftMotor.stop()

    #get ultrasonic sensor reading
    def getSensorReading(self, sensor):
        if sensor == 'front':
            reading = self.FRONT_US_SENSOR.value() /10
        elif sensor == 'right':
            reading = self.RIGHT_US_SENSOR.value() /10
        elif sensor == 'left':
            reading = self.LEFT_US_SENSOR.value() /10
        return reading
    
    




    

    
