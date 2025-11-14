from plalist_skeletons import liked_songs
import time

# A function that adds a new song to the playlist dictionary
def add_song(playlist, name, artist, minutes, seconds, genre):
    playlist[name] = {
        "artist": artist,
        "duration": (minutes, seconds),
        "genre": genre
    }
    return playlist


# A function that prints all songs in the playlist
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


# A function that checks if a song exists in the playlist
def check_song_exists(playlist, name):
    if name in playlist:
        return True
    else:
        return False


# A function that removes a song from the playlist by name
def remove_song(playlist, name):
    if check_song_exists(playlist, name):
        playlist.pop(name)
        print(f"'{name}' was removed from the playlist.")

    # Handles case where song is missing
    else:
        print(f"The song '{name}' doesn't exist in the playlist. It may have already been removed.")


# A function that removes all songs by a specific artist
def remove_artist_songs(playlist, artist_name):
    songs_to_remove = []

    # Collect all songs by the artist
    for song, details in playlist.items():
        if details["artist"] == artist_name:
            songs_to_remove.append(song)

    if not songs_to_remove:
        print(f"No songs by '{artist_name}' were found in the playlist.")
        return

    # Remove them from playlist
    for song in songs_to_remove:
        playlist.pop(song)

    print(f"All songs by '{artist_name}' were removed from the playlist.")


# Sleep Mode: simulates playing songs for a limited time
# Plays songs in order
# Prints time remaining after each song
# Stops when timer ends or playlist finishes
def sleep_mode(playlist, minutes):
    total_time = minutes * 60
    print(f"Sleep mode started for {minutes} minutes ({total_time} seconds).")
    print()

    for name, details in playlist.items():
        song_minutes, song_seconds = details["duration"]
        song_length = song_minutes * 60 + song_seconds  # Convert song length to seconds

        # If not enough time to play full song - play partially
        if total_time < song_length:
            print(f"Playing '{name}' partially...")
            print(f"Time remaining: {total_time} seconds.")
            time.sleep(total_time)  # Simulate the remaining playback time
            print("Timer ended in the middle of the song. Stopping playback.")
            return

        # Enough time to play full song
        print(f"Now playing: '{name}' ")
        print(f"Song duration: {song_length} seconds")
        print(f"Time remaining before playing: {total_time} seconds")
        print()

        time.sleep(song_length)      # Simulate full song playback
        total_time -= song_length    # Update remaining sleep timer

        # If timer ends exactly after the song
        if total_time <= 0:
            print("Timer ended exactly at the end of the song.")
            return

        print(f"Finished song. Time left: {total_time} seconds.")
        print()

    # If playlist ended but timer still has time left
    print("Playlist ended before the timer finished.")
    print(f"Time left: {total_time} seconds.")



def main():
    counter = 0

    # Getting 3 songs from the user
    while counter < 3:
        name = input("Enter the name of the song: ")
        artist = input("Enter artist name: ")

        # Edge case - validate minutes & seconds
        while True:
            minutes = int(input("Enter duration (minutes): "))
            if minutes < 0:
                print("Minutes cannot be negative. Try again.")
                continue

            seconds = int(input("Enter duration (seconds): "))
            if seconds <= 0 or seconds > 59:
                print("Seconds must be between 0 and 59. Try again.")
                continue

            break

        genre = input("Enter genre: ")
        print()

        # Add song to playlist
        add_song(liked_songs, name, artist, minutes, seconds, genre)
        counter += 1

    print_playlist(liked_songs)

    # Song check & optional removal loop
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
            # Try to remove nonexistent song (prints message)
            remove_song(liked_songs, check_song)
            print()

    print_playlist(liked_songs)

    # Remove all songs by a specific artist
    artist_input = input("Enter an artist name to remove all their songs: ")
    remove_artist_songs(liked_songs, artist_input)
    print()
    print_playlist(liked_songs)

    # Sleep timer feature
    minutes = int(input("Enter sleep timer minutes: "))
    sleep_mode(liked_songs, minutes)


main()
