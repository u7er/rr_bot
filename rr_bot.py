from pynput.mouse import Button,Controller
from pynput import keyboard
import time
import PIL.ImageGrab
import math
from threading import Thread

mouse = Controller()

timeToRestart = 340 # sec 120 sec = 7 min. 
needToRestart = False
prolongacia = 0
elapsedTime = 0
elapsedTimeCircle = 0
needToSleep = 0

def on_activate_up():
    global prolongacia
    prolongacia = prolongacia + 10
    print('up timing. Current:', prolongacia, 'All', prolongacia + timeToRestart)

def on_activate_down():
    global prolongacia
    prolongacia = prolongacia - 10
    print('down timing. Current:', prolongacia, 'All', prolongacia + timeToRestart)

def on_activate_exit():
    print('exit')
    exit(0)

def on_activate_breakon():
    global needToSleep
    print('Start the break')
    needToSleep = True

def on_activate_breakoff():
    global needToSleep
    print('End the break')
    needToSleep = False

def hotkey_listener():
    with keyboard.GlobalHotKeys(
        {
            '<ctrl>+<alt>+u': on_activate_up,
            '<ctrl>+<alt>+d': on_activate_down,
            '<ctrl>+<alt>+o': on_activate_breakon,
            '<ctrl>+<alt>+f': on_activate_breakoff,
            '<ctrl>+<alt>+e': on_activate_exit
        }
    ) as target:
        target.join()

listener_thread = Thread(target=hotkey_listener)

# True
# False
while False:
    while needToSleep:
        print('Sleeping')
        time.sleep(5)
    #mouse.position = (1336, 870)
    print(mouse.position,PIL.ImageGrab.grab().load()[mouse.position[0],mouse.position[1]])
    time.sleep(1)

listener_thread.start()
i = 1
def getColor(position):
    return PIL.ImageGrab.grab().load()[position[0],position[1]]

while(True):
    while needToSleep:
        print('Sleeping')
        time.sleep(5)
    start = time.time()
    mouse.position = (1138, 850) # start game
    for r in range(5):
        mouse.click(Button.left, 1)
        time.sleep(1)
    mouse.position = (1310, 947) # upgrade hero 5
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = (1210, 947) # upgrade hero 4
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = (1010, 947) # upgrade hero 2
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = (910, 947) # upgrade hero 1
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = (1110, 947) # upgrade hero 3
    mouse.click(Button.left, 1)
    time.sleep(1)
    #mouse.position = (1159, 587) # restart game
    #mouse.click(Button.left, 1)
    end = time.time()
    elapsedTime += end - start
    elapsedTimeCircle += end - start
    print('Iteration number:', i, 'of', (timeToRestart + prolongacia),
        'Elapsed circle:', round(elapsedTimeCircle,2), 
        'Elapsed:', round(elapsedTime,2), 
        'Added timing:',  prolongacia)
    i = i + 1
    if i > (timeToRestart + prolongacia):
        print('Got command to restart')
        mouse.position = (1408, 999)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.position = (1314, 103)
        mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.position = (1318, 422)
        mouse.click(Button.left, 1)
        time.sleep(5)
        elapsedTimeCircle = 0
        prolongacia = 0
        i = 0



