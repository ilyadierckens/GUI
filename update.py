import wget
import os



def programupdate():
    if os.path.exists("/home/pi/Program/gui.py"):
        os.remove("/home/pi/Program/gui.py")
        print('Beginning file download with wget module')
        url = 'https://drive.google.com/uc?export=download&id=1ceQ3SDkGJ-Li2f8itrhojVM5hHd4Dday'
        wget.download(url, '/home/pi/Program/gui.py')
