from hal import hal_led as led
from threading import Thread
from time import sleep

from hal import hal_keypad as keypad


def led_thread():
    global delay

    delay = 0

    while(True):
        if delay != 0:
            led.set_output(20,1)
            sleep(delay)
            led.set_output(20, 0)
            sleep(delay)

def init():

    global delay

    t1 = Thread(target=led_thread)

    t1.start()

    delay = 1


def check_keypad(lcd):
    global delay

    while(True):
        #Add code here to read from keypad and control LED

        key = keypad.get_key()

        if key == 1:
            delay = 1
            lcd.lcd_clear()
            lcd.lcd_display_string("LED Control", 1)  # write on line 1
            lcd.lcd_display_string("Blink LED",2)

        elif key == 0:
            delay = 0
            lcd.lcd_clear()
            lcd.lcd_display_string("LED Control", 1)  # write on line 1
            lcd.lcd_display_string("OFF LED",2)
