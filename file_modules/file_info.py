import os

class FileInfo:
    def __init__(self, file_path):
        assert file_path is not None
        assert file_path != ''
        
        file_location, file_name = os.path.split(file_path)
        file_name_no_ext, file_ext = os.path.splitext(file_name)

        self.full_path = file_path
        self.file_location = file_location
        self.file_name = file_name
        self.file_name_no_ext = file_name_no_ext
        self.file_ext = file_ext