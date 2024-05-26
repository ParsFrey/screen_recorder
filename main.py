import numpy as np
import pyautogui
import cv2
import time

screen_size = (1980, 1080)  # full HD!
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Corrected codec (use "XVID" or "MJPG")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

fps = 120
prev = 0  # for making the records slower

try:
    while True:
        time_elapsed = time.time() - prev

        if time_elapsed > 1.0 / fps:
            prev = time.time()
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)
        
        # This will allow a clean exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    out.release()
    cv2.destroyAllWindows()