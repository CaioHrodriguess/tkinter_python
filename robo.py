import pyautogui
from time import sleep

pyautogui.click(1242,176, duration=1)
pyautogui.press('enter')
sleep(3)
pyautogui.click(1003,619, duration=2)
pyautogui.write("caio123")

pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.click(57,45, duration=2)

#ADICIONAR ITENS
with open('itens_aleatorios.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]

        pyautogui.click(235,82, duration=1)
        pyautogui.write(id_prod)
        pyautogui.click(226,150, duration=1)
        pyautogui.write(nome)
        pyautogui.click(222,216, duration=1)
        pyautogui.write(qntd)
        pyautogui.click(252,279,duration=1)
        pyautogui.write(preco)
        #SALVAR
        pyautogui.click(248,330, duration=1)
        #ENTER
        pyautogui.press('enter')