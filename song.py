class Song:
    all = []

    def __init__(self, name):
        self.name = name
        Song.add_song_to_all(self)

    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)

    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])

big = Song("Big Energy")
touch = Song("Out of touch")
print(Song.show_song_names())