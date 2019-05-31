#Getter and setters for key environment variables, only accessible via here.

import io
import string
from custom_exceptions import ConfigFormatError

musicLibraryPath = ''
musicStagingPath = ''
toBeAddedPath = ''

'''
Updates environment config variables and writes to config file
'''
def update_env_config(musicLibrary, musicStaging, toBeAdded):
    musicLibraryPath = musicLibrary
    musicStagingPath = musicStaging
    toBeAddedPath = toBeAdded
    print(musicLibraryPath, musicStagingPath, toBeAddedPath)
    #Config file writing TBA

'''
Loads config file into env_vars variables
'''
def load_config():
    try:
        configStream = io.open("PyMusicOrg.config", "r")
    except:
        print("'pymusicorg.config' not found.")
    try:
        musicLibraryPath = process_config_line("musicLibraryPath", False, configStream)
        musicStagingPath = process_config_line("musicStagingPath", False, configStream)
        toBeAddedPath = process_config_line("toBeAddedPath", False, configStream)
    except ConfigFormatError as err:
        print("'pymusicorg.config' formatted incorrectly, please see associated exception and project readme for proper input")
        print("Error:%s; Config line affected:%s;" % (err.message, err.configLine))
    except Exception as err:
        print("Error:%s;" % (format(err)))

'''
Process config line reading
'''
def process_config_line(configElemName, emptyAllowed, configStream):
    line = str.strip(configStream.readline())
    if(not line and not emptyAllowed):
        raise ConfigFormatError(configElemName, "Config line not populated")
    return line