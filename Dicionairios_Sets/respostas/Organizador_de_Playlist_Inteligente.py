class PlaylistOrganizer:
    def __init__(self):
        self.playlist = {}

    def add_song(self, title, genre):
        if title not in self.playlist:
            self.playlist[title] = genre
            print(f'Song "{title}" added to the playlist under genre "{genre}".')
        else:
            print(f'Song "{title}" is already in the playlist.')

    def remove_song(self, title):
        if title in self.playlist:
            del self.playlist[title]
            print(f'Song "{title}" removed from the playlist.')
        else:
            print(f'Song "{title}" not found in the playlist.')

    def list_songs_by_genre(self, genre):
        print(f'Songs in genre "{genre}":')
        for title, song_genre in self.playlist.items():
            if song_genre == genre:
                print(f'- {title}')

    def list_all_songs(self):
        print('All songs in the playlist:')
        for title, genre in self.playlist.items():
            print(f'- {title} (Genre: {genre})')


if __name__ == "__main__":
    organizer = PlaylistOrganizer()
    # Example usage
    organizer.add_song("Song A", "Rock")
    organizer.add_song("Song B", "Pop")
    organizer.add_song("Song A", "Rock")  # Duplicate
    organizer.list_songs_by_genre("Rock")
    organizer.list_all_songs()
    organizer.remove_song("Song A")
    organizer.list_all_songs()