import pyautogui

xy = pyautogui.locateCenterOnScreen('aula 7/botao_8.png')
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7/x.png')
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7/2.png')
print(xy)
pyautogui.click(xy, duration=1)

xy = pyautogui.locateCenterOnScreen('aula 7/=.png')
print(xy)
pyautogui.click(xy, duration=1)