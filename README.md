# WCSU Motion Capture

[TOC]

## 1 Overview

The Raspberry Pi Motion Capture and Tracking System (name to be changed) is an affordable motion capture system that utilizes low-cost hardware with a free, open-source custom software implemented for the general purpose, educational, and hobbyist market.

## 2 Requirements and Dependencies

### 2.1. Hardware
- Raspberry Pi Zero or Zero W
- Sony IMX219 CMOS image sensor (NoIR camera)
- IR Light Ring (LISIPAROI)
- Host Computer

### 2.2 Software
- Raspbian
- Python 3
- OpenCV
- Video4Linux 

### 2.3 Casing
-

### 2.4 Miscellaneous
- IR Reflectors

### 2.5 System Requirements
- 


## 3 Setup and Installation

### 3.1 Environment
- Room must be of *at least* x sqft
- Cameras must be positioned in a way where the only possible white light is emitted/reflected from the markers ONLY.

### 3.2 Raspberry Pi Setup

### 3.3 Camera Installation

### 3.4 Software Installation

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
- Malik Roc

## 7 License
<img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="GPLv3 Logo" style="float:right;"> This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details 
