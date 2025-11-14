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


def check_song_exists(playlist, name):
    if name in playlist:
        return True
    else:
        return False


def remove_song(playlist, name):
    if check_song_exists(playlist, name):
        playlist.pop(name)
        print(f"'{name}' was removed from the playlist.")
    else:
        print(f"The song '{name}' doesn't exist in the playlist. It may have already been removed.")



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

    while True:
        check_song = input("What song would you like to check? (or enter 'stop' to stop checking) ")
        if check_song == 'stop':
            break
        if check_song_exists(liked_songs, check_song):
            print(f"The song '{check_song}' exists in the playlist.")
            print()
            remove_option = input("Do you want to remove this song? y/n: ")
            if remove_option == 'y':
                remove_song(liked_songs, check_song)
                print()
            elif remove_option == 'n':
                print()
        else:
            remove_song(liked_songs, check_song)
            print()

    print_playlist(liked_songs)


main()