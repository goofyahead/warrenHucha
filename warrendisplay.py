from sense_hat import SenseHat
import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

sense = SenseHat()
sense.set_rotation(180)
sense.load_image("fb.png")

GPIO.add_event_detect(21, GPIO.RISING)  # add rising edge detection on a channel

while True:
	time.sleep(0.1)
	
	if GPIO.event_detected(21):
		r = requests.get("http://warren.ngrok.io/coin")
		print(r.json()["value"])
		sense.load_image("smile.png")
    		print('Button pressed')
		time.sleep(2)
		sense.load_image("fb.png")

