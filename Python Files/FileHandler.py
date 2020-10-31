import datetime
from variables import distance, workoutTime, calories, averageSpeed, totalPower
def createFile():
    x = datetime.datetime.now
    f = open("WorkoutFile/Workout - "+ x.strftime("%x") + ".txt" , "a")
    f.write("Activity Date - " + x.strtime("%x"))
    f.write("Start Time - " + x.strtime("%X"))
    f.close()

def addStats ():
    f = open("WorkoutFiles/Workout - " + x.strtime("%x") + "txt" , "a")
    f.write("Time - " + str(workoutTime))
    f.write("Distance - " + str(distance))
    f.write("averageSpeed - " +str(averageSpeed))
    f.write("Calories - " + str(calories))
    f.write("Total Power - " + str(totalPower))
    f.close()
