from gpiozero import Button
from signal import pause

button = Button(16)

def say_pressed():
  print("Button was pressed")

def say_released():
  print("Button was released")

button.when_pressed = say_pressed
button.when_released = say_released

pause()
