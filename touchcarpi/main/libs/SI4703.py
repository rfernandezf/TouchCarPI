#*************************************************************************************************************
#  ________  ________  ___  ___  ________  ___  ___  ________  ________  ________  ________  ___
# |\___   ___\\   __  \|\  \|\  \|\   ____\|\  \|\  \|\   ____\|\   __  \|\   __  \|\   __  \|\  \
# \|___ \  \_\ \  \|\  \ \  \\\  \ \  \___|\ \  \\\  \ \  \___|\ \  \|\  \ \  \|\  \ \  \|\  \ \  \
#      \ \  \ \ \  \\\  \ \  \\\  \ \  \    \ \   __  \ \  \    \ \   __  \ \   _  _\ \   ____\ \  \
#       \ \  \ \ \  \\\  \ \  \\\  \ \  \____\ \  \ \  \ \  \____\ \  \ \  \ \  \\  \\ \  \___|\ \  \
#        \ \__\ \ \_______\ \_______\ \_______\ \__\ \__\ \_______\ \__\ \__\ \__\\ _\\ \__\    \ \__\
#         \|__|  \|_______|\|_______|\|_______|\|__|\|__|\|_______|\|__|\|__|\|__|\|__|\|__|     \|__|
#
# *************************************************************************************************************
#   Author: Rafael Fernández Flores (@Plata17 at GitHub)
#   Class name: SI4703.py
#   Description: This class is my own library for handle the SI4703 radio IC.
# *************************************************************************************************************

import RPi.GPIO as GPIO 
import smbus 
import time

class SI4703:

    def __init__(self):
        self.i2c = smbus.SMBus(1) #use 0 for older RasPi
        self.address = 0x10 #address of SI4703 from I2CDetect utility || i2cdetect -y 1
        self.status = 0

    def initRadio(self):

        GPIO.setmode(GPIO.BCM) #board numbering
        GPIO.setup(23, GPIO.OUT)
        GPIO.setup(0, GPIO.OUT)  #SDA or SDIO

        #put SI4703 into 2 wire mode (I2C)
        GPIO.output(0,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(23, GPIO.LOW)
        time.sleep(.1)
        GPIO.output(23, GPIO.HIGH)
        time.sleep(.1)

        print ("Initial Register Readings")
        reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
        print ("Paso 1: " + str(reg))

        #write x8100 to reg 7 to activate oscellitor
        list1 = [0,0,0,0,0,0,0,0,0,129,0]
        w6 = self.i2c.write_i2c_block_data(self.address, 0, list1)
        time.sleep(1)
        reg = self.i2c.read_i2c_block_data(self.address, 0, 32)

        print ("Paso 2: " + str(reg))

        #write x4001 to reg 2 to turn off mute and activate IC
        list1 = [1]
        #print list1
        w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
        time.sleep(.1)
        reg = self.i2c.read_i2c_block_data(self.address, 64, 32)
        print ("Paso 3: " + str(reg))
        status = 1

    def setVolume(self, volume):
        #write volume
        print ("Doing Volume lowest setting")
        list1 = [1,0,0,0,0,0,1]
        w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
        reg = self.i2c.read_i2c_block_data(self.address, 64, 32)
        print ("Paso 4: " + str(reg))

    def setChannel(self, channel):
        #write channel
        print ("Setting Channel, pick a strong one")

        nc = channel*10 #this is 101.1 The Fox In Kansas City Classic Rock!!
        nc *= 10  #this math is for USA FM only
        nc -= 8750
        nc /= 20

        nc = int(nc)

        list1 = [1,128, nc]
        #set tune bit and set channel
        w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
        time.sleep(1) #allow tuner to tune

        # clear channel tune bit
        list1 = [1,0,nc]
        w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)

        reg2 = self.i2c.read_i2c_block_data(self.address,64, 32)
        print (reg2)  #just to show final register settings

    def stopRadio(self):
        #write x4000 to reg 2 to turn off mute and activate IC
        list1 = [0]
        #print list1
        w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
        time.sleep(.1)
        reg = self.i2c.read_i2c_block_data(self.address, 0, 32)


    #You should be hearing music now!
    #Headphone Cord acts as antenna
