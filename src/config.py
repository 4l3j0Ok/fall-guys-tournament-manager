# -*- coding: utf-8 -*-
import os


# APP CONFIG
APP_NAME = "Fall Guys Tournament Manager"
APP_VERSION = 1.0
STRFTIME_FORMAT = "%d/%m/%Y - %H:%M:%S"


# PATHS
LOCALAPPDATA = os.environ.get("LOCALAPPDATA")
LOG_FILE_PATH = "{}Low\\Mediatonic\\FallGuys_client\\Player.log".format(LOCALAPPDATA)
APP_LOG_FILE_PATH = ".\\application.log"
DATA_PATH = ".\\data.json"


#MISC
GITHUB_API_URL = "https://api.github.com/repos/4l3j0Ok/fall-guys-tournament-manager/releases/latest"
GITHUB_RELEASE_DOWNLOAD_URL = "https://github.com/4l3j0Ok/fall-guys-tournament-manager/releases/download/{}/FGAntiSniper.zip"
LATEST_RELEASE_URL = "https://github.com/4l3j0Ok/fall-guys-tournament-manager/releases/latest"
