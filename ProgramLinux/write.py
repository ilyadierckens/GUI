import time
import datetime
import os


def updatemetingen(c1V,c1A,psV,psA,luV,luA,ldV,ldA,tuV,tuA,tdV,tdA):
    currentday = datetime.datetime.now().strftime("%d-%m-%y")
    currenttime = datetime.datetime.now().strftime("%d-%m-%y %H:%M")

    lastday_file = open("lastday.txt", "r")
    lastday = lastday_file.readline()
    print(lastday)
    lastday_file.close()

    lastday_file = open("lastday.txt", "w")
    lastday_file.write(currentday)
    lastday_file.close()

    if (currentday != lastday):
        os.remove(lastday + ".txt")
        print("removing old file...")



    text_file = open(currentday + ".txt", "a")
    c1 = "C1: " + str(c1V) + "V," + str(c1A) + "A"
    ps = "Ps: " + str(psV) + "V," + str(psA) + "A"
    liftup = "Liftup: " + str(luV) + "V," + str(luA) + "A"
    liftdown = "liftdown: " + str(ldV) + "V," + str(ldA) + "A"
    tiltup = "Tiltup: " + str(tuV) + "V," + str(tuA) + "A"
    tiltdown = "Tiltdown: " + str(tdV) + "V," + str(tdA) + "A"
    text_file.write(currenttime  + " =           " + c1 + "      " + ps + "      " + liftup + "      " + liftdown + "      " + tiltup + "      " + tiltdown + "\n")
    text_file.close()
