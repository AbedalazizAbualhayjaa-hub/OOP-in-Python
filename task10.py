# Task 10 - Make It Iterable

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __iter__(self):
        return iter(self.songs)


# Deliverable

playlist = Playlist([
    "Song One",
    "Song Two",
    "Song Three"
])

# __len__
print("Number of songs:", len(playlist))

# __getitem__
print("First song:", playlist[0])

# __iter__
print("Playlist:")
for song in playlist:
    print(song)
