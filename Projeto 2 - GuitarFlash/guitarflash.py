# Projeto 2 - Zerar Game Guitar Flash com PyAutoGUI
# Entender os passos manuais para depois criar o código Python.

# Verificar se há um botão com a cor correspondente dentro do círculo
# daquela cor.
import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(768,779,(0,152,0)):
        pyautogui.press('a')
        sleep(0.05)

    if pyautogui.pixelMatchesColor(858,879,(255,8,8)):
        pyautogui.press('s')
        sleep(0.05)

    if pyautogui.pixelMatchesColor(949,778,(244,244,2)):
        pyautogui.press('j')
        sleep(0.05)
