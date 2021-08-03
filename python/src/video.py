"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._flagged = False
        self._flagReason = ""

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    def flagVideo(self, reason):
        self._flagged = True
        self._flagReason = reason

    def allowVideo(self):
        self._flagged = False
        self._flagReason = ""

    def __str__(self) -> str:
        listOfTags = []
        for tag in self.tags:
            listOfTags.append(tag)

        if (self._flagged):
            return f"{self.title} ({self.video_id}) [{' '.join(listOfTags)}] - FLAGGED (reason: {self._flagReason})"

        return f"{self.title} ({self.video_id}) [{' '.join(listOfTags)}]"

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def flagged(self) -> str:
        """Returns the flag status of a video."""
        return self._flagged

    @property
    def flagReason(self) -> str:
        """Returns the flag reason of a video."""
        return self._flagReason

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
