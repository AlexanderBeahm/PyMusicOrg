from env_vars import Env_Vars
import io
import os
import zipfile
import mutagen

supported_filetypes = ['.aac','.ac3','.aiff','.flac','.mp3','.mp4','.ogg','.wav']

def recursive_folder_walk(config, current_path):
    if(current_path in config.folder_exclusions):
        pass        

    dirs = os.listdir(current_path)
    file_path_seperator = "\\"
    if(current_path.endswith("\\") or current_path.endswith("/")):
        file_path_seperator = ""

    for file in dirs:
        formatted_path = "{0}\{1}".format(current_path, file)
        if(os.path.isdir(formatted_path)):
            print("Is folder:")
            print(formatted_path)
            recursive_folder_walk(config, formatted_path)
        elif is_archive_file(formatted_path):
            print("Is archive:")
            print(formatted_path)
        elif is_audio_file(formatted_path):
            print("Is audio file:")
            print(formatted_path)
        else:
            print("Is some other file...:")
            print(formatted_path)

def is_archive_file(file_path):
    return zipfile.is_zipfile(file_path)

def is_audio_file(file_path):
    filename, file_extension = os.path.splitext(file_path)
    return file_extension in supported_filetypes

def unzip(target, destination):
    if zipfile.is_zipfile(target):
        archive = zipfile.ZipFile(target, 'r', 0, True)
        archive.extractall(destination)

while True:
    print("Hi, this is a new program that will perform the following functions...")
    print("1. Unzip and move all folders with audio files to a stagin location")
    print("2. Iterate through all folders, extract metadata")
    print("3. Transfer each album to it's correct folder in music library under '.../Artist/Album/Disc(?)/....")
    config = Env_Vars()
    #config.update_env_config("A", "B", "C")
    config.load_config()


    #Get all archive files to extract
    print(config.to_be_added_path)
    folder_list = recursive_folder_walk(config, config.to_be_added_path)

    #Extract all archive file to named to-be-added folder

    #Get all paths for folders in to-be-added that have audio files on their first child level

    #Move all of these folders to the staging location

    #Iterate through the moved folders and start metadat extraction
    
    #Group all paths by Artist-Album

    #Move each grouping, except for unfound groupings we will keep those in staging and let user know metadata isn't found

    break
