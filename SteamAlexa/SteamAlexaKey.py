import pyautogui, time as t


def Wake():
    pyautogui.keyDown('shift');
    pyautogui.keyDown('ctrl');
    pyautogui.press('j');
    pyautogui.keyUp('shift');
    pyautogui.keyUp('ctrl');
def Louder():
    pyautogui.typewrite(['volumeup'])
    pyautogui.moveTo(81, 129)
    pyautogui.click()

import serial
ser = serial.Serial('COM3', 9600)
x = ""
while True:
    x = ser.readline()
    print(x)
    if (x != ""):
        print("Alexa")
        Wake()
        t.sleep(40)
        Louder()