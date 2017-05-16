# *************************************************************************************************************
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
import threading
import smbus
import time


class SI4703:
    def __init__(self):
        self.i2c = smbus.SMBus(1)  # Use 0 for older RasPi
        self.address = 0x10  # Address of SI4703 from I2CDetect utility || i2cdetect -y 1
        self.status = 0
        self.seekFreq = 0
        # Lock for concurrency
        self.lock = 0
        # Current ticket
        self.currentTicket = 0
        # Number of tickets
        self.nTickets = 0

    def __getTicket(self):
        result = self.nTickets
        self.nTickets += 1
        return result

    def initRadio(self):
        initRadioThread = threading.Thread(target=self.__initRadioThread)
        initRadioThread.start()

    def __initRadioThread(self):
        ticket = self.__getTicket()

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if(self.lock == 0 and ticket == self.currentTicket):
            self.lock = 1
            try:
                if(self.status == 0):
                    GPIO.setmode(GPIO.BCM)  # Board numbering
                    GPIO.setup(23, GPIO.OUT)
                    time.sleep(.2)
                    GPIO.setup(0, GPIO.OUT)  # SDA or SDIO
                    time.sleep(.2)

                    # Put SI4703 into 2 wire mode (I2C)
                    GPIO.output(0, GPIO.LOW)
                    time.sleep(.2)
                    GPIO.output(23, GPIO.LOW)
                    time.sleep(.2)
                    GPIO.output(23, GPIO.HIGH)
                    time.sleep(.2)

                    reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                    time.sleep(.2)
                    # Write 8100h to 07h (Starts the crystal oscillator)
                    list1 = reg[17:28:]
                    list1[9] = 129
                    list1[10] = 0
                    w6 = self.i2c.write_i2c_block_data(self.address, 0, list1)
                    time.sleep(1)  # Wait for the crystal oscillator to stabilize.

                    # Write x4001 to 02h to turn off mute and activate IC
                    list1 = [1]
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(.2)  # Wait for device power up

                    self.status = 1

            except:
                GPIO.cleanup()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if(self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def setVolume(self, volume):
        setVolumeThread = threading.Thread(target=self.__setVolumeThread, args=(volume,))
        setVolumeThread.start()

    def __setVolumeThread(self, volume):
        ticket = self.__getTicket()

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if(self.lock == 0 and ticket == self.currentTicket):
            self.lock = 1
            try:
                if (self.status == 1):
                    # Check if the volume passed to the method is in the range of correct values
                    if (volume >= 0 or volume <= 15):
                        volumeValue = volume
                    else:
                        volumeValue = 1

                    reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                    time.sleep(.2)

                    # Write the volume(D0:D3) to 05h
                    list1 = reg[17:24:]
                    list1[6] = volumeValue
                    print(list1)
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(.2)

                    reg = self.i2c.read_i2c_block_data(self.address, 64, 32)
                    time.sleep(.2)

            except:
                GPIO.cleanup()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if (self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def setChannel(self, channel):
        setChannelThread = threading.Thread(target=self.__setChannelThread, args=(channel,))
        setChannelThread.start()

    def __setChannelThread(self, channel):
        ticket = self.__getTicket()

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if (self.lock == 0 and ticket == self.currentTicket):
            self.lock = 1
            try:
                if (self.status == 1):
                    # Math to calculate the correct frequency
                    nc = channel * 10
                    nc *= 10
                    nc -= 8750
                    nc /= 20

                    nc = int(nc)

                    # Write tune bit and channel to 03h
                    list1 = [1, 128, nc]
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(1)  # allow tuner to tune

                    # Write tune bit to low to clean it to 03h
                    list1 = [1, 0, nc]
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(.2)

            except:
                GPIO.cleanup()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if (self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def __setSeekFrequency(self, freq):
        self.seekFreq = freq

    def seekUp(self):
        seekUpThread = threading.Thread(target=self.__seekUpThread)
        seekUpThread.start()
        seekUpThread.join()
        return self.seekFreq

    def __seekUpThread(self):
        ticket = self.__getTicket()

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if (self.lock == 0 and ticket == self.currentTicket):
            self.lock = 1
            try:
                # Write 4701h to 02h
                list1 = [1]
                w6 = self.i2c.write_i2c_block_data(self.address, 71, list1)
                time.sleep(0.5)

                # Read 0Ah
                reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                time.sleep(.2)

                list1 = reg[:4:]
                print(list1)

                # Math for re-calculate the tunned channel:
                freq = list1[3]
                freq = freq * 20
                freq = freq + 8750
                freq = freq / 100

                self.__setSeekFrequency(freq)

                # Write 4001h to 02h
                list1 = [1]
                w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                time.sleep(.2)


            except:
                GPIO.cleanup()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if (self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def seekDown(self):
        seekDownThread = threading.Thread(target=self.__seekDownThread)
        seekDownThread.start()
        seekDownThread.join()
        return self.seekFreq

    def __seekDownThread(self):
        ticket = self.__getTicket()

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if (self.lock == 0 and ticket == self.currentTicket):
            self.lock = 1
            try:
                # Write 4501h to 02h
                list1 = [1]
                w6 = self.i2c.write_i2c_block_data(self.address, 69, list1)
                time.sleep(0.5)

                # Read 0Ah
                reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                time.sleep(.2)

                list1 = reg[:4:]
                print(list1)

                # Math for re-calculate the tunned channel:
                freq = list1[3]
                freq = freq * 20
                freq = freq + 8750
                freq = freq / 100

                self.__setSeekFrequency(freq)

                # Write 4001h to 02h
                list1 = [1]
                w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                time.sleep(.2)


            except:
                GPIO.cleanup()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if (self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def stopRadio(self):
        stopRadioThread = threading.Thread(target=self.__stopRadioThread)
        stopRadioThread.start()

    def __stopRadioThread(self):
        ticket = self.__getTicket()
        print("NUEVO TICKET STOP: " + str(ticket) + " CURRENT: " + str(self.currentTicket))

        while not (self.lock == 0 and ticket == self.currentTicket):
            time.sleep(0.2)

        if (self.lock == 0 and ticket == self.currentTicket):
            print("ENTRO EN STOP")
            self.lock = 1
            try:
                if (self.status == 1):
                    print("---------------- STOP RADIO -------------------")
                    # Initial reading to avoid overwrite with the wrong data other bits in other memory banks
                    reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                    time.sleep(.2)

                    # Write 7C04h to 07h (Sets AHIZEN)
                    list1 = reg[17:28:]
                    list1[9] = 124
                    list1[10] = 4
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(.2)

                    # Write 002A to 04h (Sets GPIO1/2/3 to low to reduce the current consumption)
                    reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                    time.sleep(.2)
                    list1 = reg[17:22:]
                    list1[3] = 0
                    list1[4] = 42
                    w6 = self.i2c.write_i2c_block_data(self.address, 64, list1)
                    time.sleep(.2)

                    # Write 0041h to 02h
                    list1 = [65]
                    w6 = self.i2c.write_i2c_block_data(self.address, 0, list1)
                    time.sleep(0.5)  # Wait for powerdown

                    # Last reading of all values
                    reg = self.i2c.read_i2c_block_data(self.address, 0, 32)
                    time.sleep(.2)
                    print(reg[16:28:])

                    GPIO.cleanup()

                    self.status = 0

            except:
                GPIO.cleanup()
                # TODO No se modifican los valores del finally. Modificar aquí un flag y volver a llamar a stopRadio
                # al final del finally en caso de problemas
                #self.stopRadio()

            finally:
                self.currentTicket += 1
                self.lock = 0
                if (self.currentTicket == self.nTickets):
                    self.currentTicket = 0
                    self.nTickets = 0

    def getRDSName(self):
        pass

    def getGPIOStatus(self):
        return self.status
