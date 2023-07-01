import cv2
import pyautogui
import numpy as np


def find_object(template):
    screen = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    if max_val > 0.9:  # Adjust the threshold as per your requirement
        return max_loc
    else:
        return None

def main():
    object_template = cv2.imread('x2.png', cv2.IMREAD_COLOR)
    
    while True:
        object_location = find_object(object_template)
        
        if object_location is not None:
            # Object found, move the mouse cursor and press a button
            x, y = object_location
            pyautogui.moveTo(x, y)
            pyautogui.click(button='left')
            break
        
        # Object not found, continue scanning
        
if __name__ == '__main__':
    main()
