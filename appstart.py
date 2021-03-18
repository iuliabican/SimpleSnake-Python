from ui import *


class Settings:
    def __init__(self):
        self._fileName = ""
        self._settingsDictionary = {}

    def readSettings(self):
        """
        This function reads the settings.properties file and
        returns a dictionary containing the needed info to pass to the start function
        """
        f = open("settings.properties", "r")
        line = f.readline().strip()
        settingsDictionary = dict()
        while line != "":
            if line[0] != "#":
                line = line.split("=")
                settingsDictionary[line[0].strip()] = line[1].strip().strip('""')
            line = f.readline().strip()
        f.close()
        if len(settingsDictionary) == 0:
            raise Exception("Empty settings file")
        self._settingsDictionary = settingsDictionary

    def start(self):
        """
        This function initialises the repositories according to the settings.properties file,
        and also initialises the services and the ui accordingly
        """
        self.readSettings()
        try:
            settings = self._settingsDictionary
            dimension = int(settings['DIM'])
            apple_count = int(settings['apple_count'])

            # Initialise & Start UI
            ui = UI(dimension, apple_count)
            ui.start()
        except Exception as ex:
            print(ex)


application = Settings()
application.start()
