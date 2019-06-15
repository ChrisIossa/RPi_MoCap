# RPi_MoCap
This repository contains files relating to the development of a low-cost motion capture using the Raspberry Pi range of computers. <br /> This work is being conducted as part of the Graphics Research Group at **Western Connecticut State University (WCSU)**. 

## Team Members

- SGRI 2017
	- William Joel (Faculty Advisor)
	- Paul Canada (Project Lead)
	- Christopher Iossa
	- Orquidia Moreno
	- George Ventura
- SGRI 2018 
	- William Joel (Faculty Advisor)
	- Christopher Iossa (Project Lead)
	- Matheus Alexandre
	- Ty Doris
	- Malik Roc
- SGRI 2019 
	- William Joel (Faculty Advisor)
	- Matheus Alexandre (Project Lead)
	- Malik Roc
	- Ty Doris
	


## Description
The goal of this project is to design a cost-effective motion capture system using "off the shelf" components and custom designed software. The project currently uses Raspberry Pi 3 computers for development but is targeting Raspberry Pi Zeroes for deployment. The system also uses NoIR cameras for computer vision purposes The software is written in Python and utilizes the [OpenCV computer vision library](https://opencv.org/).

## History

The initial work on the project was done during Summer 2017. At that point in time Git was not used on the project, so no commit history is available from that time. In the span of 6 short weeks a prototype system was built. This system ran the Raspbian Operating System and was capable of accessing the IR camera and controlling the IR lights. The software was able to detect and label IR reflectors (or blobs).

## Issues 

- Low Framerate on the RPi0
- CPU Overheating when light ring is in use for extended period
- Blobs are detected but not tracked
	- The blobs are labeled in raster order
	- Blobs are labeled on a per frame basis. That is, for each frame, the labels are cleared and numbering starts back at 0.
	- The camera does not detect that a blob that has moved from one frame to another is the same blob.
- The camera does not communicate with the host. In fact the host system has not even been developed.
- The camera is currently controlled via keyboard, however, the final system design should not use a keyboard
- Documentation missing
	- Code documentation is minimal and should be expanded.
	- There is no "instruction manual" for the software.
