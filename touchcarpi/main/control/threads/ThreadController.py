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
#   Description: This class is a singleton that controls all the application threads. Gives to the API global access
#   to the threads for stop them.
# *************************************************************************************************************

class ThreadController:
    """
    This class is a singleton that controls all the application threads.
    The idea is to have one set & get for each system thread.
    """

    #Singleton pattern
    class __ThreadController:

        def __init__(self):
            """
            Constructor of the thread controller.
            """

            self.reproductionStatusThread = None
            self.changeFrequencyThread = None

        def setReproductionStatusThread(self, reproductionStatusThread):
            """
            Sets the reproduction status thread current instance.
            :param reproductionStatusThread: Current thread instance.
            """

            self.reproductionStatusThread = reproductionStatusThread

        def getReproductionStatusThread(self):
            """
            Returns the current reproduction status thread instance.

            :return: Instance of a thread.
            """

            return self.reproductionStatusThread

        def setChangeFrequencyThread(self, changeFrequencyThread):
            """
            Sets the change frequency thread current instance.
            :param changeFrequencyThread: Current thread instance.
            """

            self.changeFrequencyThread = changeFrequencyThread

        def getChangeFrequencyThread(self):
            """
            Returns the current change frequency thread instance.

            :return: Instance of a thread.
            """

            return self.changeFrequencyThread


        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self):
        if not ThreadController.instance:
            ThreadController.instance = ThreadController.__ThreadController()

    def __getattr__(self, name):
        return getattr(self.instance, name)