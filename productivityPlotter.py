#to be used with export file from UltraChron Stopwatch Lite Android App

import pylab

def convertToMinutes(timeString):
    """returns time in minutes:  timeString of form 00:00'00"0
    """
    hours   = int(timeString[:2])
    minutes = int(timeString[3:5])
    seconds = int(timeString[6:8])
    millis  = int(timeString[9])

    hours   *= 60.
    seconds /= 60.
    millis  /= 60000.
    
    return hours + minutes + seconds + millis
    

lapTimes   = [0]
totalTimes = [0]

fileName = "timing.txt"

with open(fileName, 'r') as text:
    
    text = text.readlines()
    for i in text[::-1]:
        key = i[:8]
        if key == "Lap Time":
            lapTimes.append(convertToMinutes(i[-11:]))
        elif key == "Lap Tota":
            totalTimes.append(convertToMinutes(i[-11:]))

pylab.plot(totalTimes)
pylab.plot(lapTimes)

pylab.xlabel("Work Sessions")
pylab.ylabel("Minutes")

pylab.xticks(range(len(totalTimes)))

pylab.show()

