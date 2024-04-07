import pyautogui,time
import keyboard

times = int(input(">>> "))
time_s = time.time()

for i in range(times):

    if keyboard.is_pressed('shift') == True:
        print('Exited on '+str(time_s - time.time()))
        break
    else:
        pyautogui.click()
    print(end=str(i)+"\r")