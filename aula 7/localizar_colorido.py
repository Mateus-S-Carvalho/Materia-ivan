import pyautogui

xy = pyautogui.locateCenterOnScreen('aula 7/vermelho.png', confidence=0.7,grayscale=False)

pyautogui.click(xy, duration=1)