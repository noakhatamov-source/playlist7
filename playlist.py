from plalist_skeletons import liked_songs

def add_song(playlist, name, artist, minutes, seconds, genre):
    playlist[name] = {
        "artist": artist,
        "duration": (minutes, seconds),
        "genre": genre
    }
    return playlist

def print_playlist(playlist):
    print("Your Playlist:")
    print()
    for name, details in playlist.items():
        artist = details["artist"]
        minutes, seconds = details["duration"]
        genre = details["genre"]
        print(f"Name: {name}")
        print(f"Artist: {artist}")
        print(f"Duration: ({minutes}, {seconds})")
        print(f"Genre: {genre}")
        print()


def main():
    counter = 0
    while counter < 3:
        name = input("Enter the name of the song: ")
        artist = input("Enter artist name: ")
        minutes = int(input("Enter duration (minutes): "))
        seconds = int(input("Enter duration (seconds): "))
        genre = input("Enter genre: ")
        print()

        add_song(liked_songs, name, artist, minutes, seconds, genre)
        counter += 1
    print_playlist(liked_songs)

main()