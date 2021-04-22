import cv2 as cv
import datetime
import os.path



recordingFramesPerSec = 10
recordingWidth =  640
recordingheight = 480



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
    cap = cv.VideoCapture(1)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    recording = False

    while cap.isOpened():
        diff = cv.absdiff(frame1, frame2)
        diff_gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

        blur = cv.GaussianBlur(diff_gray, (5, 5), 0)
        _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        dilated = cv.dilate(thresh, None, iterations=3)
        contours, _ = cv.findContours(
            dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv.boundingRect(contour)
            if cv.contourArea(contour) < 2000:
                if (recording == True) :
                    recording  = False
                continue

            # seconds passed since epoch

            local_time = getCurrentDateTime()

            #cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(frame1, "Rec: {}".format(local_time), (20, 20), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 3)
            if (recording == False) :
                recording = True


            if (recording == True) :
                fileName = 'events/' + str(getCurrentDateAndHourMinute()) + '.avi'
                if os.path.isfile(fileName):
                    out.write(frame1)
                else:
                    out = cv.VideoWriter(fileName, cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), recordingFramesPerSec, (recordingWidth, recordingheight))
                    out.write(frame1)

        # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

        cv.imshow("Video", frame1)
        frame1 = frame2
        ret, frame2 = cap.read()

        if cv.waitKey(50) == 27:
            out.release()
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    motionDetection()