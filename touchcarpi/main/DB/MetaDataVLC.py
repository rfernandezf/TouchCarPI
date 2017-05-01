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
#   Class name: MetaDataVLC.py
#   Description: This class reads the meta data of the songs using the VLC lib.
# *************************************************************************************************************

import libs.vlc as vlc


class MetaDataVLC:
    """
    This class reads the meta data of the songs using the VLC lib.
    """

    def __init__(self, pathFiles):
        """
        Constructor of the class.

        :param pathFiles: List of strings with the path of all the files readed.
        """

        self.pathFiles = pathFiles
        self.vlcInstance = vlc.Instance()
        self.mediaList = []

        for i in range(0, len(self.pathFiles)):
            self.mediaList.append(self.vlcInstance.media_new(self.pathFiles[i]))

    def getMetaData(self):
        """
        Method that returns the meta data for all the list.

        Format of the returned list in order:
            libvlc_meta_Title
            libvlc_meta_Artist
            libvlc_meta_Genre
            libvlc_meta_Copyright
            libvlc_meta_Album
            libvlc_meta_TrackNumber
            libvlc_meta_Description
            libvlc_meta_Rating
            libvlc_meta_Date
            libvlc_meta_Setting
            libvlc_meta_URL
            libvlc_meta_Language
            libvlc_meta_NowPlaying
            libvlc_meta_Publisher
            libvlc_meta_EncodedBy
            libvlc_meta_ArtworkURL
            libvlc_meta_TrackID
            libvlc_meta_TrackTotal
            libvlc_meta_Director
            libvlc_meta_Season
            libvlc_meta_Episode
            libvlc_meta_ShowName
            libvlc_meta_Actors
            libvlc_meta_AlbumArtist
            libvlc_meta_DiscNumber
            libvlc_meta_DiscTotal

        :return: List of strings with all the meta data.
        """

        metaDataList = []
        for i in range (0, len(self.pathFiles)):
            self.media = self.mediaList[i]
            self.media.parse()

            metaData = []
            for i in range(0, 16):
                metaData.append(self.media.get_meta(i))
            metaData.append(self.media.get_duration())
            metaDataList.append(metaData)

        return metaDataList
