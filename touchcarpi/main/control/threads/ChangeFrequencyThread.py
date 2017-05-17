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
#   Class name: ChangeFrequencyThread.py
#   Description: This class is a thread runnable class that allows to switch between frequencies quickly and only tune
#   the last selected instead of tune all the frequencies between the start and the end.
# *************************************************************************************************************

import threading
import time

class ChangeFrequencyThread (threading.Thread):
    """
    This class is a thread runnable class that allows to switch between frequencies quickly.
    """

    def __init__(self, ms, freq, setCurrentFMFrequency, startGUICoolDown):
        """
        Constructor of the thread.
        """

        self.ms = ms
        self.currentFrequency = freq
        self.setCurrentFMFrequency = setCurrentFMFrequency
        self.startGUICoolDown = startGUICoolDown
        threading.Thread.__init__(self)
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

        time.sleep(self.ms)
        if(self._stop.isSet() == False):
            self.startGUICoolDown(1.3)
            self.setCurrentFMFrequency(self.currentFrequency)
