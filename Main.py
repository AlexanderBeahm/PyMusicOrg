#Main entry point and music reorg algorithm will be handled here
import env_vars


while True:
    print("Hi, this is a new program that will perform the following functions...")
    print("1. Unzip and move all folders with audio files to a stagin location")
    print("2. Iterate through all folders, extract metadata")
    print("3. Transfer each album to it's correct folder in music library under '.../Artist/Album/Disc(?)/....")
    env_vars.update_env_config("A", "B", "C")
    env_vars.load_config()
    break
