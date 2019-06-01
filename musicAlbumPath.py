from album_metadata import AlbumMetadata

class musicAlbum:
    def __init__(self, path, isZip):
        self.currentLocation = path
        self.isZip = isZip
        self.AlbumMetadata = AlbumMetadata()