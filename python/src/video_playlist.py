"""A video playlist class."""
from .video import Video


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playListName) -> None:
        self.name = playListName
        self.playList = []

    def addToPlaylist(self, video: Video):
        self.playList.append(video)

    def getPlayList(self):
        return self.playList

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self.name
