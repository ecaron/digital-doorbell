from gpiozero import PWMLED, Button
from signal import pause
import time, random

light_status = False

red_led = PWMLED(17)
blue_led = PWMLED(27)
green_led = PWMLED(22)
button = Button(16)

def button_pressed():
  global light_status
  if light_status == True:
    red_led.off()
    blue_led.off()
    green_led.off()
    light_status = False
  else:
    red_led.value = random.random()
    blue_led.value = random.random()
    green_led.value = random.random()
    print 'Color is #%02x%02x%02x' % (round(red_led.value * 255), round(green_led.value * 255), round(blue_led.value * 255))
    light_status = True

button.when_pressed = button_pressed

pause()
