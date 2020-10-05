
__author__ : '@rockdevu'

import pyautogui as pag     # pip install pyautogui
import cv2      # pip install opencv-python
import numpy as np      # pip install numpy

reso = pag.size()
video_codec = cv2.VideoWriter_fourcc(*'XVID')
file_name = 'Recording.avi'

fps = 60.0

out = cv2.VideoWriter(file_name, video_codec, fps, reso)
cv2.namedWindow('Live', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live', 480, 270)

while True:
    img = pag.screenshot()

    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live', frame)
    if cv2.waitKey(1) == ord('q'):
        break
        out.release()
        cv2.destroyAllWindows()

