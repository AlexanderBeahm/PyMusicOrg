from env_vars import Env_Vars
import io
import os
import mutagen
from pyunpack import Archive
import ntpath
from file_modules.file_info import FileInfo

supported_filetypes = ['.aac','.ac3','.aiff','.flac','.mp3','.mp4','.ogg','.wav']
supported_archives = ['.zip','.7z','.rar']

def recursive_folder_walk(config, current_path):
    if current_path in config.folder_exclusions:
        return        

    dirs = os.listdir(current_path)
    file_path_seperator = "\\"
    if current_path.endswith("\\") or current_path.endswith("/"):
        file_path_seperator = ""

    for file in dirs:
        formatted_path = "{0}\{1}".format(current_path, file)
        file_info = get_file_info(formatted_path)
        if os.path.isdir(formatted_path):
            recursive_folder_walk(config, formatted_path)
        elif is_archive_file(formatted_path):
            config.s3client.upload(file_info)
            unzip(formatted_path, config.music_staging_path)
        elif is_audio_file(formatted_path):
            pass
        else:
            pass

def get_file_info(file_path):
    return FileInfo(file_path)

def is_archive_file(file_path):
    filename, file_extension = os.path.splitext(file_path)
    return file_extension in supported_archives

def is_audio_file(file_path):
    filename, file_extension = os.path.splitext(file_path)
    return file_extension in supported_filetypes

def unzip(target, destination):
    base_filename = ntpath.basename(target)
    nested_folder = os.path.join(destination, base_filename)
    if not os.path.exists(nested_folder):
        os.mkdir(nested_folder)
    Archive(target).extractall(nested_folder)