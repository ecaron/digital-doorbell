from gpiozero import LED
import time

led = LED(26)

for x in range(3):
  led.on()
  time.sleep(1)
  led.off()
  time.sleep(1)
