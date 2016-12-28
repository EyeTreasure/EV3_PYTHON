#!/usr/bin/env python3


#EV3 demo code to demonstrate basic robot functions and use of ultrasonic sensor
#Copyright Berend Rah 2016
#as shown on Youtube
#https://www.youtube.com/watch?v=pe8zZEnMTGA


from ev3dev.auto import *
import time
import random

motors = [LargeMotor(address) for address in (OUTPUT_A, OUTPUT_B)]

assert all([m.connected for m in motors]), \
    "Two large motors should be connected to ports A and B"

btn=Button()

r=random


USS=UltrasonicSensor()
USS.mode='US-DC-CM'                  #this is continuous mode USSmodes will display all available modes

#distance is in mm NOT cm

def mDistance():
	
	try:
		return USS.value()
		time.sleep(0.3)
	
	except IOerror:   #catch connection errors
		
		pass
		
def moveThreeSecs():

        for m in motors:
                m.run_timed(time_sp=3000, speed_sp=600) # run for 3 seconds

def turnRight():
        motors[0].run_timed(time_sp=1000, speed_sp=-600)
        motors[1].run_timed(time_sp=1000, speed_sp=600)

def turnLeft():
        motors[0].run_timed(time_sp=1000, speed_sp=600)
        motors[1].run_timed(time_sp=1000, speed_sp=-600)
        


while not btn.any():

	dist=mDistance()

	if dist <1000:  #distance less than 1 meter
                choice=r.randint(0,2)
                if choice==0:
                        moveThreeSecs()
                elif choice==1:
                        turnRight()
                else:
                        turnLeft()

                time.sleep(0.3)
	

	
