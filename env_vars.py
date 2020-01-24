import io
import string
from custom_exceptions import ConfigFormatError

class Env_Vars:
    def __init__(self):
        self.music_library_path = ''
        self.music_staging_path = ''
        self.to_be_added_path = ''
        self.folder_exclusions = []


    def update_env_config(self, music_library, music_staging, to_be_added, exclusions):
        '''Updates environment config variables and writes to config file
        '''
        self.music_library_path = music_library
        self.music_staging_path = music_staging
        self.to_be_added_path = to_be_added
        self.folder_exclusions = exclusions
        print(self.music_library_path, self.music_staging_path, self.to_be_added_path, self.folder_exclusions)
        #Config file writing TBA


    def load_config(self):
        '''Loads config file into env_vars variables
        '''
        try:
            config_stream = io.open("PyMusicOrg.config", "r")
        except:
            print("'pymusicorg.config' not found.") 
            return
        try:
            self.music_library_path = self.process_config_line("musicLibraryPath", False, config_stream)
            self.music_staging_path = self.process_config_line("musicStagingPath", False, config_stream)
            self.to_be_added_path = self.process_config_line("toBeAddedPath", False, config_stream)
            exclusion_csv = self.process_config_line("excludedToBeAddedFolders", False, config_stream)
            self.folder_exclusions = exclusion_csv.split(',')
        except ConfigFormatError as err:
            print("'pymusicorg.config' formatted incorrectly, please see associated exception and project readme for proper input")
            print("Error:%s; Config line affected:%s;" % (err.message, err.configLine))
        except Exception as err:
            print("Error:%s;" % (format(err)))


    def process_config_line(self, config_elem_name, empty_allowed, config_stream):
        '''Process config line reading
        '''
        line = config_stream.readline()
        line = self.split_config_line(line)
        if(not line and not empty_allowed):
            raise ConfigFormatError(config_elem_name, "Config line not populated")
        return line


    def split_config_line(self, line_to_split):
        '''Splits config line on equals string
        '''
        line_parts = line_to_split.split('=', 1)
        stripped_line_parts = str.strip(line_parts[1]).strip('"')
        return stripped_line_parts