# AIsurvaillancesystem
A python based  survaillance system with Artificial intelligence and based on OpenCV

Ideal and tested environment :

Python 3.7.9


Install requirements :

opencv-python

The avi video's are stored in the application folders.  So make sure the folder "events" and "out" exists and that python can write to these folders.  

Run  python motionDetectionOneVideoPerDetection.py  or motionDetectionOneVideoPerHour.py


If you wish to connect to an IP camera you can use :

Make sure you install imutils (pip install imutils), because Opencv cannot decode H264 streams.  Therefore I used a different method to capture the camera stream.

python motionDetectionIpcam.py




