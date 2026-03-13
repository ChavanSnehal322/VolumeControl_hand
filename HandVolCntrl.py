#  Windows

#  using HandDetection module ( 20 LMKs)
import HandTrackingModule as HTM

import cv2
import mediapipe as mp
import numpy as np
import  time
import math # ( for Hypotenious)
# #  for volume control on windows
from pycaw.pycaw import  AudioUtilities, IAudioEndpointVolume


# width and height of the camera window display
CamWidth, CamHeight = 640, 490

#
cap = cv2.VideoCapture(0)
cap.set(3, CamWidth)
cap.set(4, CamHeight)

pTime = 0

#  object of the module
detector = HTM.detectHand(detectionCon = 0.7)

#  using pycaw library code for windows
from ctypes import cast, pointer
from comtypes import  CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)

volume = cast(interface, pointer(IAudioEndpointVolume) )
# volume.GetMute()
# # volume.GetMasterVolumeLevel()
# print(volume.GetVolumeRange() )
# setting volume of system
# # volume.SetMasterVolumeLevel(-20.0, None)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]

vol = 0
volSlider = 400
volPercent = 0


while True:

    success, img = cap.read()

    #  using the module method to detect hand lmks by pasing img and string in img
    img = detector.detect_Hand_lmks(img)

    #  position of landmarks list
    lmkList = detector.detectPosition(img, draw = False)

    # list of hand lmks values ( 21 values)
    # print(lmkList)
    #  print(lmkList[2])  # prints lmk at point 2

    if len(lmkList) != 0:
        # printing the index and thumb tip lamks only
        print(lmkList[4], lmkList[8])

        x1, y1 = lmkList[4][1], lmkList[4][2]
        x2, y2 = lmkList[8][1], lmkList[8][2]

        #  center of line
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        #  drawing circles for index and thumb tip lmk
        cv2.circle( img, (x1, y1), 9, (255, 0, 255), cv2.FILLED)
        cv2.circle( img, (x2, y2), 9, (255, 0, 255), cv2.FILLED)

        #  printing the line between the two finger tips
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        #  circle for the center of line
        cv2.circle(img, (cx, cy), 9, (255, 0, 0), cv2.FILLED)

        #  length of the line
        length = math.hypot(x2 - x1, y2 - y1)

        #  converting hand range ( 50 to 100) to fit vol range to -65 to -0
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        volSlider = np.interp(length[50, 300], [400, 150])

        volPercent = np.interp(length, [50, 300], [0, 100])

        print(int(length), vol)

        volume.setMasterVolumeLevel(vol, None)

        #  if the vol is < 50 , changing the lmk of center of line
        if length < 50 and length > 1:
            cv2.circle(img, (cx, cy), 9, (0, 255, 0), cv2.FILLED)

        if length == 0:
            cv2.circle(img, (cx, cy), 2, (0, 0, 255), cv2.FILLED)

    #      printing volume slider
    cv2.rectangle(img, (50, 150), (80, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volSlider)), (80, 400), (255, 0, 0), cv2.FILLED)

    #  volume percent
    cv2.putText(img, f'FPS : {int(volPercent)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    #  curr time
    cTime = time.time()

    # Calculating the fps
    fps = 1 / (cTime - pTime)

    pTime = cTime

    # printing the fps values
    cv2.putText(img, f'FPS : {int(fps) }', (40, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)

    cv2.waitKey(1)