from env_vars import Env_Vars
from file_staging import recursive_folder_walk

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

    #Iterate through the moved folders and start metadat extractions
    
    #Group all paths by Artist-Album

    #Move each grouping, except for unfound groupings we will keep those in staging and let user know metadata isn't found

    break
