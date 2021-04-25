"""
This code uses connects to a standard USB camera.
Be sure you use the correct recordingWidth and recordingHeight that corresponds with the camera stream.

Look at the installation procedure to use this code on a Raspberry Pi (installOnRaspberryPi.txt)

"""


import cv2 as cv
import datetime
import os.path
from imutils.video import VideoStream
import time
from gpiozero import CPUTemperature


recordingFramesPerSec = 10
recordingWidth =  640
recordingheight = 480
camName = 'USB'




def getCurrentDateTime() :
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    second = '{:02d}'.format(now.second)
    currentDateTime = '{}-{}-{} {}:{}:{}'.format(year, month, day,hour,minute,second)
    return currentDateTime

def getCurrentDateAndHourMinute() :
    now = datetime.datetime.now()
    year = '{:02d}'.format(now.year)
    month = '{:02d}'.format(now.month)
    day = '{:02d}'.format(now.day)
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    returnString = '{}{}{}{}{}'.format(year, month, day,hour,minute)
    return returnString


def motionDetection():

    #cap = cv.VideoCapture(0)
    cap = VideoStream("/dev/video0").start()
    time.sleep(2.0)
    


    frame1 = cap.read()
    frame2 = cap.read()


    recording = False

    fourcc = cv.VideoWriter_fourcc(*'MP4V')



    while True:
        diff = cv.absdiff(frame1, frame2)
        diff_gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

        blur = cv.GaussianBlur(diff_gray, (5, 5), 0)
        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations=3)
        contours, _ = cv.findContours(
            dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        local_time = getCurrentDateTime()
        cv.putText(frame1, camName+ ": {}".format(local_time), (40, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cpu = CPUTemperature()
        cv.putText(frame1, "CPU: " + str(round(cpu.temperature,0)), (40, 440), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)


        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            if cv.contourArea(contour) < 20000:
                if (recording == True) :
                    recording  = False
                continue

            # seconds passed since epoch

            #cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if (recording == False) :
                recording = True


            if (recording == True) :
                fileName = 'events/'+ camName+ '_' + str(getCurrentDateAndHourMinute()) + '.mp4'
                if os.path.isfile(fileName):
                    out.write(frame1)
                else:
                    out = cv.VideoWriter(fileName, fourcc, recordingFramesPerSec, (recordingWidth, recordingheight))
                    out.write(frame1)
                cv.putText(frame1, "Recording", (40, 80), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                #cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)




        cv.imshow("Video", frame1)
        frame1 = frame2
        frame2 = cap.read()

        if cv.waitKey(50) == 27:
            #out.release()
            break

    cap.stream.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    motionDetection()