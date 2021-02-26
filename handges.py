import serial                                      # add Serial library for serial communication
import time
import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.

ArduinoSerial = serial.Serial('com3',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
time.sleep(2)
while 1:
    incoming_data = str (ArduinoSerial.readline()) # read the serial data and print it as line
    print (incoming_data)                            # print the incoming Serial data
     

    if 'Play/Pause' in incoming_data:                    # if incoming data is 'next'
        pyautogui.typewrite(['space'],0.2)           # perform "ctrl+pgdn" operation which moves to the next tab
        
    if 'VDown' in incoming_data:                # if incoming data is 'previous'
        pyautogui.typewrite(['f8'],0.2)       # perform "ctrl+pgup" operation which moves to the previous tab
       
    if 'Mute' in incoming_data:                # if incoming data is 'previous'
        pyautogui.typewrite(['f7'],0.2)               # perform "ctrl+pgup" operation which moves to the previous tab
    
    if 'Vup' in incoming_data:                    # if incoming data is 'down'
        #pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.typewrite(['f9'],0.2) 
         
    if 'forward' in incoming_data:                      # if incoming data is 'up'
        #pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        pyautogui.typewrite(['f11'],0.2)
        
    if 'change' in incoming_data:                  # if incoming data is 'change'
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
    incoming_data = "";                            # clears the data
