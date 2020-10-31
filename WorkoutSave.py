import datetime

def startWorkout():
    x = datetime.datetime.now
    f = open(x.strftime("%c") + ".txt" , "w")
    f.write("Activity Date - " + x.strtime("%x"))
    f.write("Start Time - " + x.strtime("%X"))
    f.close()
