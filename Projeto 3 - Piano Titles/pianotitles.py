# Zerar Game Piano Titles com PyAutoGUI
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep
import webbrowser

webbrowser.open_new_tab('https://littlegames.gg/game/halloween-piano-tiles/#')
sleep(2)
pyautogui.click(939,507, duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(821,369, (235,97,35)):
        click(821,369)

    if pyautogui.pixelMatchesColor(914,381, (235,97,35)):
        click(914,381)

    if pyautogui.pixelMatchesColor(996,384, (235,97,35)):
        click(996,384)

    if pyautogui.pixelMatchesColor(1079,387, (235,97,35)):
        click(1079,387)
