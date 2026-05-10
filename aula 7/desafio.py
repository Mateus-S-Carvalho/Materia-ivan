import pyautogui

while True:
    xy = pyautogui.locateCenterOnScreen('aula 7/bolinha.png', confidence=0.5,grayscale=False)

    pyautogui.click(xy, duration=0)