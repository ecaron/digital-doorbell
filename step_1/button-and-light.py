from gpiozero import LED, Button
from signal import pause
import time

led = LED(26)
button = Button(16)

def button_pressed():
  for x in range(3):
    led.on()
    time.sleep(.5)
    led.off()
    time.sleep(.5)

def button_released():
  for x in range(2):
    led.on()
    time.sleep(2)
    led.off()
    time.sleep(2)

button.when_pressed = button_pressed
button.when_released = button_released

pause()
