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
#   Class name: ReproductionStatusThread.py
#   Description: This class is a thread runnable class that polls the actual reproduction second.
# *************************************************************************************************************

import threading
import time

class ReproductionStatusThread (threading.Thread):
    """
    This class is a thread runnable class that polls the actual reproduction second.
    """

    def __init__(self, mediaPlayer, notifyAudioController):
        """
        Constructor of the thread.

        :param mediaPlayer: Media Player instance for poll the second.
        :param notifyAudioController: Method to notify of the changes to the Audio Controller.
        """

        threading.Thread.__init__(self)
        self.mediaPlayer = mediaPlayer
        self.notifyAudioController = notifyAudioController
        self._stop = threading.Event()

    def stop(self):
        """
        Stop method of the thread.
        """

        self._stop.set()

    def run(self):
        """
        Run method of the thread.
        """

        #print ("Starting " + self.name)
        while self._stop.isSet() == False:
            miliseconds = self.mediaPlayer.get_time()
            self.notifyAudioController("updateReproductionSecond", miliseconds)
            time.sleep(0.100)
        #print ("Exiting " + self.name)
