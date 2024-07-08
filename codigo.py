import pyautogui
import time

# pyautogui.click  - clicar com o mouse
# pyautogui.write  - escrever textos
# pyautogui.press  - pressionar 1 tecla
# pyautogui.hotkey - combinação de teclas (Ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

# Passo 1 - Entrar no sistema da empresa
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# time.sleep(2)

# Passo 1 Fim


