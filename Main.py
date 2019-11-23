def recursive_folder_walk(currentPath):
    dirs = os.listdir(config.toBeAddedPath)
    filePathSeperator = "\\"
    if(config.toBeAddedPath.endswith("\\") or config.toBeAddedPath.endswith("/")):
        filePathSeperator = ""

    for file in dirs:
        formattedPath = "{0}\{1}".format(currentPath, file)
        if(os.path.isdir(formattedPath)):
            recursive_folder_walk(formattedPath)
        else:
            pass #TBC
        print(os.path.isdir(formattedPath))
        print(formattedPath)

def is_archive_file(filePath):
    pass

def is_audio_file(filePath):
    pass


#Main entry point and music reorg algorithm will be handled here
from env_vars import Env_Vars
import io
import os

while True:
    print("Hi, this is a new program that will perform the following functions...")
    print("1. Unzip and move all folders with audio files to a stagin location")
    print("2. Iterate through all folders, extract metadata")
    print("3. Transfer each album to it's correct folder in music library under '.../Artist/Album/Disc(?)/....")
    config = Env_Vars()
    config.update_env_config("A", "B", "C")
    config.load_config()


    #Get all archive files to extract
    print(config.toBeAddedPath)
    folderList = recursive_folder_walk(config.toBeAddedPath)

    #Extract all archive file to named to-be-added folder

    #Get all paths for folders in to-be-added that have audio files on their first child level

    #Move all of these folders to the staging location

    #Iterate through the moved folders and start metadat extraction
    
    #Group all paths by Artist-Album

    #Move each grouping, except for unfound groupings we will keep those in staging and let user know metadata isn't found

    break
