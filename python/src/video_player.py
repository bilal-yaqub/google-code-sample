"""A video player class."""

from .video_playlist import Playlist
from .video_library import VideoLibrary
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.currentlyPlaying = ""
        self.currentlyPaused = ""
        self.playListNames = []
        self.playLists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")
        for video in self._video_library.get_sorted_videos():
            print(video)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        for video in self._video_library.get_all_videos():
            if (video.video_id == video_id):
                if self.currentlyPlaying != "":
                    print(f"Stopping video: {self.currentlyPlaying}")

                if self.currentlyPaused != "":
                    print(f"Stopping video: {self.currentlyPaused}")

                print(f"Playing video: {video.title}")
                self.currentlyPlaying = video.title
                return

        print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.currentlyPlaying != "":
            print(f"Stopping video: {self.currentlyPlaying}")
            self.currentlyPlaying = ""
            return

        if self.currentlyPaused != "":
            print(f"Stopping video: {self.currentlyPaused}")
            self.currentlyPaused = ""
            return

        print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        randomNumber = randint(
            0, (len(self._video_library.get_all_videos()) - 1))
        randomVideo = self._video_library.get_all_videos()[randomNumber].title

        if self.currentlyPlaying != "":
            print(f"Stopping video: {self.currentlyPlaying}")

        self.currentlyPlaying = randomVideo
        print(f"Playing video: {randomVideo}")

    def pause_video(self):
        """Pauses the current video."""

        if self.currentlyPaused != "":
            print(f"Video already paused: {self.currentlyPaused}")
            return

        if self.currentlyPlaying != "":
            self.currentlyPaused = self.currentlyPlaying
            self.currentlyPlaying = ""

            print(f"Pausing video: {self.currentlyPaused}")
            return

        print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.currentlyPlaying != "":
            print("Cannot continue video: Video is not paused")
            return

        if self.currentlyPaused != "":
            print(f"Continuing video: {self.currentlyPaused}")
            self.currentlyPlaying = self.currentlyPaused
            self.currentlyPaused = ""
            return

        print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if (self.currentlyPaused != "") or (self.currentlyPlaying != ""):
            for video in self._video_library.get_all_videos():
                if (video.title == self.currentlyPlaying) or (video.title == self.currentlyPaused):
                    if self.currentlyPlaying != "":
                        print(
                            f"Currently playing: {video}")
                        return
                    if self.currentlyPaused != "":
                        print(
                            f"Currently playing: {video} - PAUSED")
                        return

        print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        modified_playlist_name = playlist_name.lower()
        for playList in self.playLists:
            if playList.title == modified_playlist_name:
                print(
                    "Cannot create playlist: A playlist with the same name already exists")
                return

        self.playLists.append(Playlist(modified_playlist_name))
        self.playListNames.append(playlist_name)

        print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        modified_playlist_name = playlist_name.lower()

        for playList in self.playLists:
            if playList.title == modified_playlist_name:
                for video in playList.getPlayList():
                    if video.video_id == video_id:
                        print(
                            f"Cannot add video to {playlist_name}: Video already added")
                        return

                for video in self._video_library.get_all_videos():
                    if video.video_id == video_id:
                        playList.addToPlaylist(video)
                        print(f"Added video to {playlist_name}: {video.title}")
                        return

                print(
                    f"Cannot add video to {playlist_name}: Video does not exist")
                return

        print(f"Cannot add video to {playlist_name}: Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        if self.playListNames == []:
            print("No playlists exist yet")
            return

        print("Showing all playlists: ")
        for playList in sorted(self.playListNames, key=str.lower):
            print(playList)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        modified_playlist_name = playlist_name.lower()
        for playList in self.playLists:
            if modified_playlist_name == playList.title:
                if playList.getPlayList() == []:
                    print(f"Showing playlist: {playlist_name}")
                    print(" No videos here yet")
                    return

                print(f"Showing playlist: {playlist_name}")
                for video in playList.getPlayList():
                    print(
                        f"  {video}")
                return

        print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        videoExists = False
        modified_playlist_name = playlist_name.lower()

        for video in self._video_library.get_all_videos():
            if video.video_id == video_id:
                videoExists = True

        if videoExists == False:
            print(
                f"Cannot remove video from {playlist_name}: Video does not exist")
            return

        for playList in self.playLists:
            if playList.title == modified_playlist_name:
                for video in playList.getPlayList():
                    if video.video_id == video_id:
                        print(
                            f"Removed video from {playlist_name}: {video.title}")
                        playList.removeFromPlaylist(video)
                        return

                print(
                    f"Cannot remove video from {playlist_name}: Video is not in playlist")
                return

        print(
            f"Cannot remove video from {playlist_name}: Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        modified_playlist_name = playlist_name.lower()

        for playList in self.playLists:
            if playList.title == modified_playlist_name:
                print(f"Successfully removed all videos from {playlist_name}")
                playList.clearPlaylist()
                return

        print(
            f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        modified_playlist_name = playlist_name.lower()

        for playList in self.playLists:
            if playList.title == modified_playlist_name:
                print(f"Deleted playlist: {playlist_name}")
                self.playLists.remove(playList)
                return

        print(
            f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        index = 1
        listOfTitles = []
        listOfMatchesVideos = []

        for video in self._video_library.get_all_videos():
            listOfTitles.append(video.title)

        for word in sorted(listOfTitles, key=str.lower):
            for video in self._video_library.get_all_videos():
                if word == video.title:
                    if ((search_term.lower()) in (video.title.lower())):
                        if index == 1:
                            print(f"Here are the results for {search_term}:")
                        listOfTags = []
                        for tag in video.tags:
                            listOfTags.append(tag)
                        print(
                            f"  {index}) {video.title} ({video.video_id}) [{' '.join(listOfTags)}]")
                        listOfMatchesVideos.append(video)
                        index += 1

        if listOfMatchesVideos != []:
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            option = input()
            try:
                option = int(option)
                if option <= len(listOfMatchesVideos):
                    video = listOfMatchesVideos[option - 1]
                    print(
                        f"Playing video: {video.title}")
                    return
                else:
                    raise ValueError
            except ValueError:
                return

        print(f"No search results for {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        index = 1
        listOfTitles = []
        listOfMatchesVideos = []

        for video in self._video_library.get_all_videos():
            listOfTitles.append(video.title)

        for word in sorted(listOfTitles, key=str.lower):
            for video in self._video_library.get_all_videos():
                if word == video.title:
                    listOfTags = []
                    listOfLowerTags = []
                    for tag in video.tags:
                        listOfTags.append(tag)
                        listOfLowerTags.append(tag.lower())

                    if video_tag.lower() in listOfLowerTags:
                        if index == 1:
                            print(f"Here are the results for {video_tag}:")
                        print(
                            f"  {index}) {video.title} ({video.video_id}) [{' '.join(listOfTags)}]")
                        listOfMatchesVideos.append(video)
                        index += 1

        if listOfMatchesVideos != []:
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            option = input()
            try:
                option = int(option)
                if option <= len(listOfMatchesVideos):
                    video = listOfMatchesVideos[option - 1]
                    print(
                        f"Playing video: {video.title}")
                    return
                else:
                    raise ValueError
            except ValueError:
                return

        print(f"No search results for {video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
