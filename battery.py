import datetime
import time
import psutil


filename = "battery.txt"


out_file = open(filename,"w")
loop = True


while loop:
    battery = psutil.sensors_battery()
    percent = battery.percent
    datetimenow = datetime.datetime.now()
    indata = f"DateTime: {datetimenow} - {percent}% battery\n"
    out_file.write(indata)
    print(indata)
    time.sleep(60)
    if percent < 10:
        loop = False






