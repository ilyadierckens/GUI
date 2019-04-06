import wget
import urllib
import os



def programupdate():
    if os.path.exists("/home/pi/ProgramLinux/gui.py"):
        os.remove("/home/pi/ProgramLinux/gui.py")
        print('Beginning file download...')
        url = 'https://raw.githubusercontent.com/ilyadierckens/GUI/master/ProgramLinux/gui.py'
        urllib.request.urlretrieve(url, "gui.py")
        print("Download complete!...")

    else:
        print("Path to gui script not found!...")
