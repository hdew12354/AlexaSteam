import pyautogui as p, time as t
print(p.KEY_NAMES)
p.typewrite(['volumeup'])
#p.moveTo(81, 83)
#p.click()
p.moveTo(1040, 813)
p.click()
print("noise on")
p.moveTo(1405, 891)
for i in range(20):
    p.dragTo(1405, 891)
    p.dragTo(1496, 885)
