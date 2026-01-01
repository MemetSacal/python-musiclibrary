from music_library import MusicLibrary
from song import Song
import time

def show_menu():
    print("\nMusic Library")
    print("1 - Add song")
    print("2 - List all songs")
    print("3 - Delete song")
    print("4 - Play song")
    print("5 - Add song to favorites")
    print("6 - List favorite songs")
    print("7 - Show total duration")
    print("8 - Show song links")
    print("0 - Exit")

def main():
    library = MusicLibrary()

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            title = input("Title: ")
            artist = input("Artist: ")
            album = input("Album: ")
            producer = input("Production company: ")
            duration = int(input("Duration (seconds): "))
            spotify = input("Spotify URL: ")
            apple = input("Apple Music URL: ")

            song = Song(
                song_id=None,
                title=title,
                artist=artist,
                album=album,
                production_company=producer,
                duration=duration,
                spotify_url=spotify if spotify else None,
                apple_music_url=apple if apple else None,
                play_count=0,
                is_favorite=False
            )

            library.add_song(song)
            print("Song added successfully")
            time.sleep(1)

        elif choice == "2":
            library.list_songs()
            time.sleep(1)

        elif choice == "3":
            song_id = int(input("Song ID to delete: "))
            library.delete_song(song_id)
            print("Song deleted")
            time.sleep(1)

        elif choice == "4":
            song_id = int(input("Song ID to play: "))
            library.play_song(song_id)
            print("Song played")
            time.sleep(1)

        elif choice == "5":
            song_id = int(input("Song ID to add to favorites: "))
            library.add_to_favorites(song_id)
            print("Added to favorites")
            time.sleep(1)

        elif choice == "6":
            library.list_favorites()
            time.sleep(1)

        elif choice == "7":
            library.total_duration()
            time.sleep(1)

        elif choice == "8":
            song_id = int(input("Song ID: "))
            library.show_song_links(song_id)
            time.sleep(1)


        elif choice == "0":
            library.close_connection()
            print("Goodbye, keep the music alive")
            break

        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
