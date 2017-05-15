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
#   Class name: UtilityFunctions.py
#   Description: A tiny library with utility functions used by some classes
# *************************************************************************************************************

import platform

def getBandName(metaData):
    """
    Gets the metaData string of a band name and returns a string without null values

    :param metaData: Original band meta data string.
    :return: String with the name of the band without null values.
    """

    if metaData == None:
        value = "Artista desconocido"
    else:
        value = metaData

    return value

def getArtworkPath(metaData):
    path = []

    if (metaData[15] == None):
        path = "themes/default/img/artworkNotFound.png"
    else:
        if platform.system() == "Windows":
            path = metaData[15][8::]
        elif platform.system() == "Linux":
            path = metaData[15][7::]
        path = path.replace("%20", " ")

    return path