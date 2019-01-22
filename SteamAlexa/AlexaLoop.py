import pyautogui, time as t
def Wake():
    pyautogui.keyDown('shift');
    pyautogui.keyDown('ctrl');
    pyautogui.press('j');
    pyautogui.keyUp('shift');
    pyautogui.keyUp('ctrl');

while 1:
    Wake()
    t.sleep(45)