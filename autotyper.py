import pyautogui as py
import time 
a = input("Enter the Sentence :")
time.sleep (10) 
for _ in range(int(input("Enter how many times"))):
    py.write(a) 
    py.press("enter")
