#1 - Navegar até o site https://www.instagram.com
import webbrowser
import pyautogui
from time import sleep

webbrowser.open('https://www.instagram.com/')
sleep(1.5)
#2 - Entrar com o usuário
pyautogui.click(1065,423, duration=1.5)
sleep(1.5)
pyautogui.typewrite('19999231013')
#3 - Entrar com a senha
pyautogui.click(1059,469, duration=1.5)
sleep(1.5)
pyautogui.typewrite('yxhrkbir')
sleep(1.5)
#4 - Clicar em "Log In"
pyautogui.click(1119,511, duration=1.5)
sleep(7)
#5 - Clicar em "Not now" para não salvar os dados no navegador.
pyautogui.click(1107,610, duration=1.5)
sleep(7)
#6 - Fechar janela de "salvar senha" (NÃO APARECEU)
#7 - Pesquisar pela página desejada
pyautogui.click(48,266, duration=1.5)
sleep(1.5)
pyautogui.typewrite('nike')
sleep(1.5)
#8 - Entrar na página
pyautogui.hotkey('tab')
sleep(0.5)
pyautogui.hotkey('tab')
sleep(0.5)
pyautogui.hotkey('enter')
sleep(7)
#9 - Clicar na postagem mais recente
pyautogui.click(791,751, duration=1.5)
sleep(10)
#10 - Verificar se o post ja foi curtido ou não
pyautogui.locateCenterOnScreen('coracao.png')
sleep(2)
#11 - Caso tenha curtido o post, não fazer nada, e pausar o bot por 24 horas
if coracao is not None:
    sleep(86400)
#12 - Se não tiver curtido, curtid o post
elif coracao == None:
    pyautogui.click(1091,883, duration=1.5)
    sleep(7)
    #13 - Se não tiver curtido, comentar a foto
    pyautogui.click(1133,888, duration=1.5)
    sleep(7)
    #14 - Pausar por 24 horas
#15 - Após as 24 horas, rodar tudo de novo
