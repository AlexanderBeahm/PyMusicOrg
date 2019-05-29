#Getter and setters for key environment variables, only accessible via here.

import io

musicLibraryPath = ''
musicStagingPath = ''
toBeAddedPath = ''


def UpdateEnvironmentPaths(musicLibrary, musicStaging, toBeAdded):
    musicLibraryPath = musicLibrary
    musicStagingPath = musicStaging
    toBeAddedPath = toBeAdded
    print(musicLibraryPath, musicStagingPath, toBeAddedPath)

def LoadConfigFile():
    try:
        configStream = io.open("pymusicorg.config", "r")
        line = configStream.readline()   
    except:
        print("'pymusicorg.config' not found.")
