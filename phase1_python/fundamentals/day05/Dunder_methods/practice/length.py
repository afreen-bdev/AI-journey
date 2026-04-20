class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

p = Playlist(["song1", "song2", "song3"])
print("Total songs:", len(p))