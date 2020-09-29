from gpiozero import LED, Button
from signal import pause
from dotenv import load_dotenv
from twilio.rest import Client
import time, os

load_dotenv()

start_time = 0

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

led = LED(26)
button = Button(16)

def button_pressed():
  global start_time
  start_time = time.time()
  for x in range(3):
    led.on()
    time.sleep(.2)
    led.off()
    time.sleep(.2)

def button_released():
  held_time = round(time.time() - start_time, 2)
  text = "Button was pressed. It was held for {} seconds".format(held_time)
  print 'About to text message: "{}"'.format(text), 
  message = client.messages.create(
    body=text,
    from_='+19528007375',
    to='+16127302513')
  print(" - successfully texted")
  led.on()
  time.sleep(2)
  led.off()

button.when_pressed = button_pressed
button.when_released = button_released

pause()
