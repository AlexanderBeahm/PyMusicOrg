from album_metadata import AlbumMetadata

class musicAlbum:
    def __init__(self, path, is_zip):
        self.current_location = path
        self.is_zip = is_zip
        self.album_metadata = album_metadata()