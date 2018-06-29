# WCSU Motion Capture

[TOC]

## 1 Overview

The Raspberry Pi Motion Capture and Tracking System (name to be changed) is an affordable motion capture system that utilizes low-cost hardware with a free, open-source custom software implemented for the general purpose, educational, and hobbyist market.

## 2 Requirements and Dependencies

### 2.1. Hardware
- Raspberry Pi 3 (testing done on RPi Zero)
- Sony IMX219 CMOS image sensor (NoIR camera)
- IR Light Ring (LISIPAROI)
- Host Computer

### 2.2 Software
- Raspbian
- Python 3
- OpenCV
- Video4Linux 
- VNC Viewer

### 2.3 Casing
- 3D Printed designs

### 2.4 Miscellaneous
- IR Reflectors
- HDMI cable
- Ethernet CAT.6 cable
- 40pin Jumper wires (F/F, M/M, and M/F)
- SD Card (minimum of 8gb)
- Router or Switch (for the network)

### 2.5 System Requirements
- Monitor
- Mouse
- Keyboard
- Computer that supports VNC Viewer


## 3 Setup and Installation

### 3.1 Environment
- Room must be dim; only light source should come from behind the cameras towards the markers. Any other light source will confuse the software thresholds.
- Cameras must not be parallel, otherwise triangulation is impossible.

### 3.2 Raspberry Pi Setup
- Connect the Pi to a power source.
- Connect the Pi to an network switch or router. The host computer and all other cameras should also be connected to this network.
- If the IP address of the Pi is known and VNC is enabled, connect to the Pi using VNC Viewer.
    - Otherwise, connect the Pi to a Keyboard, Mouse, and monitor. The Pi should be connected to the monitor ___before___ being powered on, otherwise video output may be disabled.
    - Ensure that VNC, SSH, and Remote GPIO are enabled under Raspberry Pi settings
    - Connect to the Pi using VNC Viewer
    - The Pi may now be disconnnected from the Monitor, Keyboard, and Mouse

### 3.3 Camera Installation
(NOTE: THIS SHOULD BE DONE WHILE THE Pi IS POWERED DOWN)
- Connect the NoIR camera to the "Camera" port in the Pi.
- Connect the IR Light Ring to the Pi via F/F breadboard cables:
    - Red F/F on pin 2
    - Black F/F on pin 6
    - Yellow F/F on pin 7
    - Pinout reference can be found on pinout.xyz
    
### 3.4 Software Installation
- Install VNC Viewer in the Host Machine
    - Connect to the Pi by inputting its IP Address onto VNC
- Make sure that all files listed on ##4 are all in the same directory/folder. This should be the latest version of the software
- Run the file "RunCamera.py" with the following parameters:
- python ./RunCamera.py [threshold value] [camera IP address] [camera Port Number] [camera Label]
    - Example: python ./RunCamera.py 255 123.456.789.000 12345 B
    
    

## 4 Files
- Marker.py
    - The class that stores data pertaining to each individual marker
- MotionCapture.py
    - Utilizing the openCV library for tracking and displaying, this is the "driver" class where all the work is done for capturing data.
- RunCamera.py
    - Script that enables the cameras to be turned on for capturing.
- enableCameraDriver.sh
    - Bash script that enables the camera driver to be utilized by host computer.

## 5 Key Bindings

|    Key     |                              Action                             | 
|------------|-----------------------------------------------------------------|
|     S      |          Writes a still image from the camera to drive          |
|     F      |               Toggles the display of FPS counter                |
|     M      |           Displays markers in view of the video frame           |
|     E      |              Enable the light-ring for the camera               |
|     D      |             Disable the light-ring for the camera               |
|  Up-Arrow  |          Decrease the threshold of whitelight capture           |
| Down-Arrow |          Increase the threshold of whitelight capture           |
|     Q      |Close down the video frame, stop capturing, and disable lightring|

## 6 Authors
### SGRI 2017
- William Joel (Faculty Advisor)
- [Paul Canada (Project Lead)](https://github.com/PaulCanada)
- [Christopher Iossa]((https://github.com/ChrisIossa))
- Orquidia Moreno
- [George Ventura](https://github.com/GeorgeVentura)
### SGRI 2018 
- William Joel (Faculty Advisor)
- [Christopher Iossa (Project Lead)](https://github.com/ChrisIossa)
- [Matheus Alexandre](https://github.com/madatedeus)
- Ty Doris
- [Malik Roc](https://github.com/rocstory)

## 7 License
<img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="GPLv3 Logo" style="float:right;"> This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details 
