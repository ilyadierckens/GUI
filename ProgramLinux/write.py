import time
import datetime
import os


looptime = 0


def drawbar():
    currentday = datetime.datetime.now().strftime("%d-%m-%y")

    text_file = open("metingen.txt", "a")
    text_file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" + "\n")
    text_file.close()






def updatemetingen(c1V,c1A,psV,psA,liftupV,liftupA,tiltupV,tiltupA,liftdownV,liftdownA,tiltdownV,tiltdownA,V3rdV,A3rdA,V4thV,A4thA):
    global looptime
    global currentday

    currentday = datetime.datetime.now().strftime("%d-%m-%y")
    currenttime = datetime.datetime.now().strftime("%d-%m-%y %H:%M")

    lastday_file = open("lastday.txt", "r")
    lastday = lastday_file.readline()
    lastday_file.close()

    lastday_file = open("lastday.txt", "w")
    lastday_file.write(currentday)
    lastday_file.close()

    if (currentday != lastday):
        print("last date: " + lastday)
        os.remove("metingen.txt")
        print("removing old file...")

    if (looptime == 0):
        print("currentday: " + currentday)
        looptime = 1




    text_file = open("metingen.txt", "a")
    c1 = "C1: " + str(c1V) + "V," + str(c1A) + "A"
    ps = "Ps: " + str(psV) + "V," + str(psA) + "A"
    liftup = "Liftup: " + str(liftupV) + "V," + str(liftupA) + "A"
    liftdown = "liftdown: " + str(liftdownV) + "V," + str(liftdownA) + "A"
    tiltup = "Tiltup: " + str(tiltupV) + "V," + str(tiltupA) + "A"
    tiltdown = "Tiltdown: " + str(tiltdownV) + "V," + str(tiltdownA) + "A"
    rd = "3rd: " + str(V3rdV) + "V," + str(A3rdA) + "A"
    th = "4th: " + str(V4thV) + "V," + str(A4thA) + "A"
    text_file.write(currenttime  + " =     " + c1 + "      " + ps + "      " + liftup + "      " + liftdown + "      " + tiltup + "      " + tiltdown + "      " + rd +  "      " + th + "\n")
    text_file.close()
