import wget
import os



def programupdate():
    if os.path.exists("/home/pi/Program/gui.py"):
        os.remove("/home/pi/Program/gui.py")
        print('Beginning file download with wget module')
        url = 'https://drive.google.com/file/d/1HhWztvqTAz7ADXgvQJjAzxXXV1lky0Q1/view?usp=sharing'
        wget.download(url, '/home/pi/Program/gui.py')

    else:
        print("Path to python script not found...")
