import sqlite3
from song import Song

class MusicLibrary:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):
        self.connection = sqlite3.connect("music.db")
        self.cursor = self.connection.cursor()

        query = ("CREATE TABLE IF NOT EXISTS music (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT,"
                 " album TEXT, production_company TEXT, duration INT, spotify_url TEXT, apple_music_url TEXT,"
                 " play_count INT, is_favorite INT)")

        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def add_song(self, song: Song):
        query = """
                INSERT INTO music (title, artist, album, production_company, \
                                   duration, spotify_url, apple_music_url, \
                                   play_count, is_favorite)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) \
                """
        self.cursor.execute(query, (
            song.title,
            song.artist,
            song.album,
            song.production_company,
            song.duration,
            song.spotify_url,
            song.apple_music_url,
            song.play_count,
            int(song.is_favorite)
        ))
        self.connection.commit()

    def list_songs(self):
        query = "SELECT * FROM music"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print("Music library is empty.")
            return

        for row in rows:
            song = Song(
                song_id=row[0],
                title=row[1],
                artist=row[2],
                album=row[3],
                production_company=row[4],
                duration=row[5],
                spotify_url=row[6],
                apple_music_url=row[7],
                play_count=row[8],
                is_favorite=bool(row[9])
            )
            print(song)

    def delete_song(self, song_id):
        query = "DELETE FROM music WHERE id = ?"
        self.cursor.execute(query, (song_id,))
        self.connection.commit()

    def play_song(self, song_id):
        query = "UPDATE music SET play_count = play_count + 1 WHERE id = ?"
        self.cursor.execute(query, (song_id,))
        self.connection.commit()

    def total_duration(self):
        query = "SELECT SUM(duration) FROM music"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]

        if result is None:
            print("No songs in library.")
            return

        minutes = result // 60
        seconds = result % 60
        print(f"Total duration: {minutes} min {seconds} sec")

    def add_to_favorites(self, song_id):
        query = "UPDATE music SET is_favorite = 1 WHERE id = ?"
        self.cursor.execute(query, (song_id,))
        self.connection.commit()

    def list_favorites(self):
        query = "SELECT * FROM music WHERE is_favorite = 1"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            print("No favorite songs.")
            return

        for row in rows:
            song = Song(
                song_id=row[0],
                title=row[1],
                artist=row[2],
                album=row[3],
                production_company=row[4],
                duration=row[5],
                spotify_url=row[6],
                apple_music_url=row[7],
                play_count=row[8],
                is_favorite=True
            )
            print(song)

    def show_song_links(self, song_id):
        query = """
                SELECT spotify_url, apple_music_url
                FROM music
                WHERE id = ? \
                """
        self.cursor.execute(query, (song_id,))
        result = self.cursor.fetchone()

        if result is None:
            print("Song not found.")
            return

        spotify, apple = result
        print(f"Spotify: {spotify or 'Not available'}")
        print(f"Apple Music: {apple or 'Not available'}")

