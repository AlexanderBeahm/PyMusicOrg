#Getter and setters for key environment variables, only accessible via here.

import io
import string
from custom_exceptions import ConfigFormatError

class Env_Vars:
    def __init__(self):
        self.musicLibraryPath = ''
        self.musicStagingPath = ''
        self.toBeAddedPath = ''

    '''
    Updates environment config variables and writes to config file
    '''
    def update_env_config(self, musicLibrary, musicStaging, toBeAdded):
        musicLibraryPath = musicLibrary
        musicStagingPath = musicStaging
        toBeAddedPath = toBeAdded
        print(musicLibraryPath, musicStagingPath, toBeAddedPath)
        #Config file writing TBA

    '''
    Loads config file into env_vars variables
    '''
    def load_config(self):
        try:
            configStream = io.open("PyMusicOrg.config", "r")
        except:
            print("'pymusicorg.config' not found.") 
            return
        try:
            self.musicLibraryPath = self.process_config_line("musicLibraryPath", False, configStream)
            self.musicStagingPath = self.process_config_line("musicStagingPath", False, configStream)
            self.toBeAddedPath = self.process_config_line("toBeAddedPath", False, configStream)
        except ConfigFormatError as err:
            print("'pymusicorg.config' formatted incorrectly, please see associated exception and project readme for proper input")
            print("Error:%s; Config line affected:%s;" % (err.message, err.configLine))
        except Exception as err:
            print("Error:%s;" % (format(err)))

    '''
    Process config line reading
    '''
    def process_config_line(self, configElemName, emptyAllowed, configStream):
        line = configStream.readline()
        line = self.split_config_line(line)
        line = str.strip(line)
        if(not line and not emptyAllowed):
            raise ConfigFormatError(configElemName, "Config line not populated")
        return line

    '''
    Splits config line on equals string
    '''
    def split_config_line(self, lineToSplit):
        lineParts = lineToSplit.split('=', 1)
        strippedLineParts = str.strip(lineParts[1], '"')
        return strippedLineParts