# VolumeControl_hand

System volume controller using Hand Gesture

A **Computer Vision** based system that allows users to control their system volume using hand gestures captured through a webcam. The application detects hand landmarks using MediaPipe and dynamically adjusts system volume based on the distance between the thumb and index finger.

This project demonstrates real time gesture recognition, computer vision processing, and OS level automation.

---------------------------------------------------------------------------------------------------
**Features**

- Real-time hand tracking using MediaPipe
- Detects 21 hand landmarks
- Adjusts system volume based on finger distance
- Interactive volume slider UI
- Displays volume percentage and FPS
- Works with macOS system volume via AppleScript
- Smooth gesture-based control

---------------------------------------------------------------------------------------------------
**How It Works**

- The webcam captures live video frames using OpenCV
- MediaPipe Hands detects hand landmarks in real time
    The positions of:
  
      a) Thumb tip (Landmark 4)
  
      b) Index finger tip (Landmark 8) are extracted.

- The Euclidean distance between these two points is calculated
- The distance is mapped to a volume percentage (0–100) using NumPy interpolation
- The volume is updated using AppleScript commands on macOS
- A visual volume slider is rendered on the screen

---------------------------------------------------------------------------------------------------
**Tech Stack** 

- Python
- OpenCV
- MediaPipe
- NumPy
- AppleScript (macOS system control)

---------------------------------------------------------------------------------------------------
**Project Structure** 

HandVolumeController/

    │
    ├── HandVolControl.py        # Main application
    
    ├── HandVolCntrl.py          # run this file if installing the project on Windows system
    
    ├── HandTrackingModule.py    # Hand detection module
    
    ├── README.md

---------------------------------------------------------------------------------------------------
**Installation**

1] Clone the repository

    > git clone https://github.com/yourusername/hand-volume-controller.git
    
    > cd hand-volume-controller
    
2] Create a virtual environment and activating it 

    > python -m venv venv
    
    > source venv/bin/activate
    
3] Install dependencies

    > pip install opencv-python mediapipe numpy

4] Run the Project

    > python HandVolControl.py

* Your webcam will open and you can control the system volume using your hand gesture.
* Open the volume display of your system to see real time upates to the volume.

---------------------------------------------------------------------------------------------------
**Gesture Control** 

Gesture	Actions:

    1] Thumb + Index finger close	Volume Low
    
    2] Thumb + Index finger far	    Volume High

---------------------------------------------------------------------------------------------------
* Sample Output

  Live webcam feed
  Hand landmarks visualization
  Gesture line between fingers
  Dynamic volume slider
  FPS display


---------------------------------------------------------------------------------------------------
**Applications**

- Touchless interfaces
- Gesture controlled systems
- Accessibility tools
- Smart home control
- Computer vision experimentation

  
