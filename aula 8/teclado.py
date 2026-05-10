import pyautogui
import time

#pressiona junto teclas windows e d 
#win + d
def abriBrave():
    pyautogui.hotkey('win', 'd')
    pyautogui.press('win')
    pyautogui.write('brave')
    pyautogui.press('enter')
    time.sleep(1)
    # pyautogui.hotkey('win', 'up')

def pesquisarGPT():
    pyautogui.write('http://www.chatgpt.com')
    pyautogui.press('enter')
    time.sleep(3)


    pyautogui.write(pesquisa)
    pyautogui.press('enter')

    while True:
        try:
            xy = pyautogui.locateCenterOnScreen('aula 8/copiar.png', confidence=0.7)
            pyautogui.click(xy)
            break
        except:
            pyautogui.press('pagedown')

def enviarEmail():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)

    pyautogui.write('www.gmail.com')
    pyautogui.press('enter')
    time.sleep(3)
    xy = pyautogui.locateCenterOnScreen('aula 8/escrever.png', confidence=0.95)
    pyautogui.click(xy)
    time.sleep(2)
    pyautogui.write('samuelazevedo29062012@gmail.com')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write('cola da prova do ivan')
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    xy = pyautogui.locateCenterOnScreen('aula 8/enviar.png',confidence=0.9)
    pyautogui.click(xy)


pesquisa = pyautogui.prompt('Oque deseja saber hoje? ')
abriBrave()
pesquisarGPT()
enviarEmail()