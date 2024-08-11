import cv2
import time
import gesture_recog as ht
import pyautogui

# Variables Declaration
pTime = 0               # Used to calculate frame rate
width = 640             # Width of Camera 640
height = 480            # Height of Camera 480
frameR = 144            # Frame Rate
prev_command_time = time.time()  # Previous command time
command_interval = 1     # Command interval in seconds

cap = cv2.VideoCapture(1)   # Getting video feed from the webcam
cap.set(3, width)           # Adjusting size
cap.set(4, height)

# Detecting one hand at max
detector = ht.handDetector(maxHands=1)
screen_width, screen_height = pyautogui.size()      # Getting the screen size

while True:
    success, img = cap.read()
    img = detector.findHands(img)                       # Finding the hand
    lmlist, bbox = detector.findPosition(img)           # Getting position of hand

    if len(lmlist) != 0:
        fingers = detector.fingersUp()      # Checking if fingers are upwards

        # Previous track: Index finger only
        if fingers[1] == 1:
            current_time = time.time()
            if current_time - prev_command_time > command_interval:
                pyautogui.hotkey('shift', 'p')
                prev_command_time = current_time

        # Play/pause: Thumb 
        if fingers[0] == 1:
            current_time = time.time()
            if current_time - prev_command_time > command_interval:
                pyautogui.press('space')
                prev_command_time = current_time

        # Next track: ring finger N
        elif fingers[4] == 1:
            current_time = time.time()
            if current_time - prev_command_time > command_interval:
                pyautogui.hotkey('shift', 'n')
                prev_command_time = current_time

        # Volume up: Thumb up gesture
        # if fingers[0] == 1:
        #     current_time = time.time()
        #     if current_time - prev_command_time > command_interval:
        #         pyautogui.press('volumeup')
        #         prev_command_time = current_time

        # # Volume down: Thumb down gesture
        # if fingers[0] == 0:
        #     current_time = time.time()
        #     if current_time - prev_command_time > command_interval:
        #         pyautogui.press('volumedown')
        #         prev_command_time = current_time

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
