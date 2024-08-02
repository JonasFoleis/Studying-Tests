'''
QUAIS OS PASSOS MANUAIS PARA ENVIO DE MENSAGEM PARA VÁRIAS
PESSOAS?

- LISTA DE NÚMEROS
- ENVIAR INDIVIDUALMENTE UMA MENSAGEM PARA CADA CONTATO
- PAUSAR ENTRE CADA ENVIO

1 - ESCOLHER UM CONTATO
2 - ENVIAR MENSAGEM PARA ESSE CONTATO
	https://api.whatsapp.com/send?phone=55191237467
3 - REPETIR O PROCESSO PARA OUTROS CONTATOS.
'''
import webbrowser
import pyautogui
from time import sleep

#telefones = []
telefones = []
with open('fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)


for telefone in telefones:
    webbrowser.open_new_tab(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    pyautogui.click(1042,248, duration=1)
    sleep(10)
    pyautogui.click(567,1015, duration=1)
    sleep(10)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(Digite sim, caso queira participar)')
    sleep(5)
    pyautogui.hotkey('enter')
    sleep(300)
