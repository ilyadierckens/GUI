import wget
import os



def programupdate():
    if os.path.exists("/home/pi/ProgramLinux/gui.py"):
        os.remove("/home/pi/ProgramLinux/gui.py")
        print('Beginning file download with wget module')
        url = 'https://drive.google.com/file/d/1ceQ3SDkGJ-Li2f8itrhojVM5hHd4Dday/view?usp=sharing'
        wget.download(url, '/home/pi/ProgramLinux/gui.py')

    else:
        print("Path to python script not found...")
