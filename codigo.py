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
# # time.sleep(2)

# # Passo 1 Fim

# # Passo 2 - Logar no Sistema

pyautogui.hotkey("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.hotkey("tab")
pyautogui.write("minha senha")
pyautogui.hotkey("enter")

# Passo 2 Fim

# Passo 3 - Importar a base de dados

import pandas

tabelaProdutos = pandas.read_csv("C:\Codigos\Jornada Python\BancoDados\produtos.csv")

print(tabelaProdutos)

# Passo 3 Fim|

# Passo 4 - Cadastrar Produto em massa

for linha in tabelaProdutos.index:


    pyautogui.click(x=2107, y=-624)
    codigo = str(tabelaProdutos.loc[linha,"codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str(tabelaProdutos.loc[linha,"marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabelaProdutos.loc[linha,"tipo"])
    pyautogui.write(tipo)
    Celular 
    pyautogui.press("tab")
    categoria = str(tabelaProdutos.loc[linha,"categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco = str(tabelaProdutos.loc[linha,"preco_unitario"])
    pyautogui.write(preco)

    pyautogui.press("tab")
    custo = str(tabelaProdutos.loc[linha,"custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabelaProdutos.loc[linha,"obs"])
    pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 4 Fim