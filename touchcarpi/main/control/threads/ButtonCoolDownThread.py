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
#   Class name: ButtonCoolDownThread.py
#   Description: This class is a thread runnable class that do a delay for cooldown some buttons of the GUI.
# *************************************************************************************************************

import threading
import time

class ButtonCoolDownThread (threading.Thread):
    """
    This class is a thread runnable class that do a delay for cool down some buttons of the GUI.
    """

    def __init__(self, ms, setGUICoolDown):
        """
        Constructor of the thread.
        """
        self.ms = ms
        self.setGUICoolDown = setGUICoolDown
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

        self.setGUICoolDown(True)
        # Half second of cooldown
        time.sleep(self.ms)
        self.setGUICoolDown(False)