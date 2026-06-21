import pyautogui
import time

pyautogui.press('win')
pyautogui.write('paint')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt','space')
time.sleep(1)
pyautogui.press('x')


largura, altura = pyautogui.size()

larguraX = largura / 2
alturaX = altura / 2

pyautogui.click(larguraX,alturaX)
pyautogui.moveTo(larguraX, alturaX)

pyautogui.dragRel(0, 100)
pyautogui.dragRel(100, 0)
pyautogui.dragRel(0, -100)
pyautogui.dragRel(-100, 0)

pyautogui.moveRel(50,-150)

pyautogui.dragRel(100, 150)
pyautogui.dragRel(-200, 0)
pyautogui.dragRel(100, -150)

xy = pyautogui.locateCenterOnScreen('balde.png',grayscale=False, confidence=0.9)
pyautogui.click(xy)

xy = pyautogui.locateCenterOnScreen('marrom.png', grayscale=False, confidence=0.9)
pyautogui.click(xy)


pyautogui.click(1000, 600, clicks=2)

xy = pyautogui.locateCenterOnScreen('verde.png', grayscale=False, confidence=0.9)
pyautogui.click(xy)


pyautogui.click(1000, 500, clicks=2)

pyautogui.hotkey('ctrl','s')
time.sleep(2)

pyautogui.write("C:\\Users\\15940727603\\Documents\\ivan\\imagemResultado.png")
pyautogui.press('enter')