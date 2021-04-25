# AIsurvaillancesystem
A python based  survaillance system with Artificial intelligence and based on OpenCV.  It can run on a standard PC and on a Raspberry Pi.  Installation procedures are included.  It should work out of the box.


Ideal and tested environment :

Python 3.7.9


Install requirements :

opencv-python

The avi video's are stored in the application folders.  So make sure the folder "events" and "out" exists and that python can write to these folders.  

Run  

    python motionDetectionOneVideoPerDetection.py
    
    or
    
    python motionDetectionOneVideoPerHour.py


If you wish to connect to an IP camera you can use :

Make sure you install imutils (pip install imutils), because Opencv cannot decode H264 streams.  Therefore I used a different method to capture the camera stream.

    pi@raspberrypi: python motionDetectionIpcam.py


Howto get it working on a raspberry PI?


Best is that you install a new fresh Raspberry Pi system visit rpf.io/download
Install Raspberry Pi  Imager and place the Raspberry Pi OS (32-bit) on a flash card


The system is designed for Python3 (3.7.9).  This version is already installed on the OS by default, but it is not set as the standard. To make it the standard version you need to create a symbolic link.

Open a terminal screen and enter :
    
    pi@raspberrypi: rm /usr/bin/python
    pi@raspberrypi: ln -s /usr/bin/python3 ~/bin/python
    


The same you need to do  for pip (installation manager)

    rm /usr/bin/pip
    ln -s /usr/bin/pip3 ~/bin/pip
    
    

To check you can run :
    
pi@raspberrypi: python --version
You should see :  Python 3.x.x


pi@raspberrypi: pip --version
You should see :  ...... (Python 3.x)


Your system is now ready to start with OPENCV and AI (Artificial intelligence) based scripts




It is time to install OpenCV:

Install some nessecary libs :
    pi@raspberrypi: sudo apt-get install libatlas-base-dev


Install opencv:
    
    pi@raspberrypi: pip install opencv-python
    
Install imutils (used for Video) :
    pi@raspberrypi: pip install imutils
    
    
To connect to a USB camera (not this standard RaspiCam) :  https://www.raspberrypi.org/documentation/usage/webcams/

    pi@raspberrypi: sudo apt install fswebcam

    
To monitor the CPU :
    
    pi@raspberrypi: pip install gpiozero
    
    

Now connect your USB webcam to you PY and launch :
    
    
    pi@raspberrypi: python motionDetectionUsbCam.py
    

At the same time you can launch another session to view an IP camera :
    
    pi@raspberrypi: python motionDetectionIpcam.py








