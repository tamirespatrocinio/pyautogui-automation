import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.click(x=2172, y=68) 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(6)

pyautogui.click(x=2466, y=402)

pyautogui.write("user@teste.com")
pyautogui.press("tab")  
pyautogui.write("password")
pyautogui.click(x=2673, y=567)  
time.sleep(3)

import pandas as pd
table = pd.read_csv("products-test.csv")
print(table)


for linha in table.index:
    
    pyautogui.click(x=2426, y=294)
    
    codigo = table.loc[linha, "codigo"]
    
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(table.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = table.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(table.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  
        
    pyautogui.scroll(5000)
