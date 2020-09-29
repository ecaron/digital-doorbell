from gpiozero import LED, Button
from signal import pause
from dotenv import load_dotenv
import time, os, tweepy

load_dotenv()

start_time = 0

auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_token"), os.getenv("access_token_secret"))

api = tweepy.API(auth)

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
  tweet = "Button was pressed. It was held for {} seconds".format(held_time)
  print 'About to tweet message: "{}"'.format(tweet), 
  api.update_status(tweet)
  print(" - successfully tweeted")
  led.on()
  time.sleep(2)
  led.off()

button.when_pressed = button_pressed
button.when_released = button_released

pause()
