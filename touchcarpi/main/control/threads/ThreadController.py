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
#   Description: This class is a singleton that controlls al the application threads. Gives to the API global access
#   to the threads for stop them.
# *************************************************************************************************************

class ThreadController:

    class __ThreadController:
        def __init__(self):
            self.reproductionStatusThread = None

        def setReproductionStatusThread(self, reproductionStatusThread):
            self.reproductionStatusThread = reproductionStatusThread

        def getReproductionStatusThread(self):
            return self.reproductionStatusThread


        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not ThreadController.instance:
            ThreadController.instance = ThreadController.__ThreadController()

    def __getattr__(self, name):
        return getattr(self.instance, name)