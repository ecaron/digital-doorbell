# Digital Doorbell

This source code will accompany a PowerPoint presentation to discuss "Don't Be Afraid of Tech".
It will show how combine multiple, small pieces of technology is the recipe for very cool stuff.
This project relies on Python (v2) to do the demos, but almost any logic would get the job done.

## Source Used

* [Raspberry Pi](https://www.raspberrypi.org/) - Basic computer to test on
* [Adafruit Starter Kit](https://www.adafruit.com/?q=starter+kit&sort=BestMatch) - Provides great hardware to play with
* [Twitter Developer API](https://developer.twitter.com/) - Used for reading & writing tweets
* [Twilio](https://www.twilio.com/) - Service to send text messages

## Steps

### Step 1
This folder includes the scripts for knowing if a button is pressed and to turn on a light.

### Step 2
This folder includes the scripts to read & write tweets.

### Step 3
This folder includes a script to measure time, and then a combination script to write a tweet & turn on a light when a button is pushed.

### Step 4
This folder includes a way to use a multicolor LED and a script to send a text message when a button is pushed.
It also includes a README linking to more complex Raspberry Pi examples.

### Note
To avoid including passwords in a repository, we're using [python-dotenv](https://pypi.org/project/python-dotenv/) to keep a .env file with the relevant Twitter & Twilio access keys.

## Reference Material
* https://gpiozero.readthedocs.io/en/stable/recipes.html
* https://www.raspberrypi.org/documentation/usage/gpio/
