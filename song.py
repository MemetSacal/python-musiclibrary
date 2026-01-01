class Song:
    def __init__(self,title,artist,album,production_company,duration,
        spotify_url=None,
        apple_music_url=None,
        song_id=None,
        play_count=0,
        is_favorite=False
    ):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.production_company = production_company
        self.duration = duration  # second type
        self.spotify_url = spotify_url
        self.apple_music_url = apple_music_url
        self.play_count = play_count
        self.is_favorite = is_favorite

    def __str__(self):
        favorite_status = "Yes" if self.is_favorite else "No"

        return (
            f"ID: {self.song_id}\n"
            f"Title: {self.title}\n"
            f"Artist: {self.artist}\n"
            f"Album: {self.album}\n"
            f"Production Company: {self.production_company}\n"
            f"Duration: {self.duration} seconds\n"
            f"Play Count: {self.play_count}\n"
            f"Favorite: {favorite_status}\n"
            f"Spotify: {self.spotify_url or 'Not available'}\n"
            f"Apple Music: {self.apple_music_url or 'Not available'}\n"
            "-----------------------------"
        )
