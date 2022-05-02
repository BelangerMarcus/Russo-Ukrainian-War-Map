import os
import requests
import shutil
from datetime import date

def download_image(url, directory, fname=None):
    if fname == None:                                            # if i don't specify a name, it will make a fileName that based on the url (super long)
        fname = os.path.basename(url)

    downloaded_img_path = os.path.join(directory, fname)         # creates fileName for the downloaded photo
    with requests.get(url, stream=True) as request:              # this keeps the request open so I can use the ".raw"
        with open(downloaded_img_path, 'wb') as file_obj:        # opens the downloaded photo fileName and prepares it to "written on"
            shutil.copyfileobj(request.raw, file_obj)            # puts the "raw" image (content) into the file
    return downloaded_img_path




today = date.today()
str_today = str(today) + '.png'

THIS_FILE_PATH = os.path.abspath(__file__)           # file path of "C:\Users\mbela\30days\RussoUkraineWar\dailydownload.py"
# print(THIS_FILE_PATH)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)           # one level above: "C:\Users\mbela\30days\RussoUkraineWar"
# print(BASE_DIR)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "mapDaily")   # writes fileName within the directory (makes a file in the same level as this code)
# print(DOWNLOADS_DIR)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)            # creates the "mapDaily" file

url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Russo-Ukraine_Conflict_%282014-present%29.svg/1280px-Russo-Ukraine_Conflict_%282014-present%29.svg.png"



download_image(url, DOWNLOADS_DIR, str_today)

