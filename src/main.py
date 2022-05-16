
# System imports
from time import sleep

# Local imports
from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_keypad as keypad

import led_control as led_ctrl



def main():
    #Initiallize LED driver
    led.init()

    #Initiallize Keypad driver
    keypad.init()

    # Instantiate and initialize the LCD driver
    lcd = LCD.lcd()

    sleep(0.5)
    lcd.backlight(0)  # turn backlight off

    sleep(0.5)
    lcd.backlight(1)  # turn backlight on

    #Clear LCD and display message
    lcd.lcd_clear()
    lcd.lcd_display_string("DevOps for AIoT", 1)  # write on line 1
    lcd.lcd_display_string("Lab 5", 2)  # write on line 2

    led_ctrl.init()
    led_ctrl.check_keypad(lcd)


# Main entry point
if __name__ == "__main__":
    main()

