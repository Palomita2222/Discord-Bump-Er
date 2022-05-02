import os
import random
from time import sleep
import pyautogui
from colorama import Fore

banner = """

 ________  ___  ___  _____ ______   ________                _______   ________     
|\   __  \|\  \|\  \|\   _ \  _   \|\   __  \              |\  ___ \ |\   __  \    
\ \  \|\ /\ \  \\\  \ \  \\\__\ \  \ \  \|\  \ ____________\ \   __/|\ \  \|\  \   
 \ \   __  \ \  \\\  \ \  \\|__| \  \ \   ____\\____________\ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \\\  \ \  \    \ \  \ \  \___\|____________|\ \  \_|\ \ \  \\  \| 
   \ \_______\ \_______\ \__\    \ \__\ \__\                  \ \_______\ \__\\ _\ 
    \|_______|\|_______|\|__|     \|__|\|__|                   \|_______|\|__|\|__|                                                                                                             

"""
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTMAGENTA_EX+banner)
times = int(input(Fore.LIGHTBLUE_EX+"Cuantas veces quieres BUMP? (Mas de 5 puede ser arriesgado) > "))
i=0
random_click = int(input(Fore.LIGHTBLUE_EX+"Este programa se ejecutara cada hora, pero para que no detecte que es un bot, necesitamos esperar un tiempo aleatorio despues de cada hora. Ese tiempo es en (s). Cuantos segundos serán el máximo de tiempo aleatorio? > "))
print(Fore.LIGHTRED_EX+"Tienes 5 seg para ir a discord (RECUERDA DE CLICAR A LA BARRA DE TEXT) > ")
sleep(5)
pyautogui.write('/bump')
pyautogui.keyDown('enter')
pyautogui.keyDown('enter')
print(Fore.LIGHTGREEN_EX+"Succesfully bumped 1 time!")
while i < times:
    secs = random.randint(1,random_click)
    sleep(secs + 3600)
    pyautogui.write('/bump')
    pyautogui.keyDown('enter')
    pyautogui.keyDown('enter')
    print(Fore.LIGHTGREEN_EX+"Succesfully bumped ",end="")
    print(i+2,end="")
    print(" times!")
    i+=1