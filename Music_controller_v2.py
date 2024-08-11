import cv2
import time
import gesture_recog  as ht
import pyautogui
import webbrowser
url = r"https://www.youtube.com/watch?v=pxwm3sqAytE&list=RDGMEMHDXYb1_DDSgDsobPsOFxpAVMpxwm3sqAytE&index=2"

pTime = 0               
width = 640             
height = 480            
frameR = 144            

command_interval = 1    

cap = cv2.VideoCapture(0)   
cap.set(3, width)           
cap.set(4, height)


detector = ht.handDetector(maxHands=1)
screen_width, screen_height = pyautogui.size()      
flag=False
while True:
    success, img = cap.read()
    img = detector.findHands(img)                       
    lmlist, bbox = detector.findPosition(img)           
 
    if len(lmlist) != 0:
        fingers = detector.fingersUp()      

        if not flag and fingers[4] == fingers[0]==1 and  fingers[1]==fingers[2] ==fingers[3] ==0 :
            print('Opening chrome with the music playlist')
            webbrowser.open(url, new=2)
            flag=True
            time.sleep(command_interval)
        elif fingers[1] ==fingers[2] ==1 and  fingers[3]==fingers[4] ==fingers[0] ==0 :
            pyautogui.press('space')
            print('Space')
            time.sleep(command_interval)


        elif fingers[4] == fingers[1]==1 and  fingers[3]==fingers[2] ==fingers[0] ==0 :
            pyautogui.hotkey('up')
            print('Up')
            time.sleep(0.5)

 
        elif fingers[2] == fingers[3]==1 and  fingers[0]==fingers[1] ==fingers[4] ==0 :
            pyautogui.hotkey('down')
            print('Down')
            time.sleep(0.5)


        elif fingers[1] == 1 and  fingers[3]==fingers[2] ==fingers[0] ==fingers[4]==0 :
            pyautogui.hotkey('shift', 'p')
            print('Shift+P')
            time.sleep(command_interval)


        elif fingers[4] == 1 and  fingers[3]==fingers[2] ==fingers[0] ==fingers[1]==0 :
            pyautogui.hotkey('shift', 'n')
            print('Shift+N')
            time.sleep(command_interval)

        elif fingers[1] ==fingers[0] ==1 and  fingers[3]==fingers[4] ==fingers[2] ==0 :
            pyautogui.press('ctrl','w')
            print('Space')
            time.sleep(command_interval)
            flag=False
        

    


    cTime = time.time()
    fps = 1/(cTime-pTime) 
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)