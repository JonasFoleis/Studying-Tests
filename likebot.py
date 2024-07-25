# 1 - Navegar até o site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(2)
    # 2 - Entrar com meu usuário
    pyautogui.click(1065,419,duration=1.5)
    sleep(2)
    pyautogui.typewrite('constru.alfa')
    sleep(2)
    # 3 - Entrar com a minha senha
    pyautogui.click(1061,465,duration=1.5)
    sleep(2)
    pyautogui.typewrite('yxhrkbir123')
    sleep(2)
    # 4 - Clicar em "log in"
    pyautogui.click(1060,516,duration=1.5)
    sleep(10)
    # 5 - Clicar em "Not now" para não salvar navegador
    pyautogui.click(1107,610,duration=1.5)
    sleep(10)
    # 6 - fechar janela de "salvar senha"
    #pyautogui.click(1662,88,duration=1)
    sleep(2)
    # 7 - Pesquisar pela pagina'
    pyautogui.click(48,266,duration=1.5)
    sleep(2)
    pyautogui.typewrite('nike')
    sleep(2)
    # 8 - Entrar na página
    pyautogui.hotkey('tab')
    sleep(2)
    pyautogui.hotkey('tab')
    sleep(2)
    pyautogui.hotkey('enter')
    sleep(10)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(1106,741,duration=1.5)
    sleep(10)
    # 10 - Verificar se já curti ou não aquela postagem
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(5)
    # 11 - Se já tiver curtido, fazer nada, e pausar o bot por 24 horas
    if coracao is not None:
        sleep(86400)
    # 12 - Se não tiver curtido, curtir a foto
    elif coracao == None:
        pyautogui.click(1091,883,duration=1.5)
        sleep(5)
        # 13 - Se não tiver curtido, comentar na foto
        pyautogui.click(1133,888,duration=1.5)
        sleep(3)
        pyautogui.click(1568,834,duration=1.5)
        sleep(2)
        pyautogui.typewrite('Gostei dessa foto!')
        sleep(5)
        pyautogui.hotkey('enter')
        #pyautogui.click(1715,832,duration=1.5)
        # 14 - Pausar por 24 horas
        sleep(86400)
