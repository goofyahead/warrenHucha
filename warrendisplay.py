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
currentCompany = "none"

while True:
	time.sleep(0.5)

	# check amount of coins and value
	r = requests.get("http://warren.ngrok.io/hucha")
	print(r.json()["value"])

	currentCompany = r.json()["company"]

	sense.show_message("Coins: " + str(r.json()["value"]), text_colour=[0, 255, 0])

	sense.show_message("Investing: " + currentCompany, text_colour=[0, 255, 0])

	if (r.json()["coeficient"] > 1):
		sense.load_image("arrow_up.png")
	else:
		sense.load_image("arrow_down.png")

	if GPIO.event_detected(21):
		requests.post("http://warren.ngrok.io/coin", data = {"key":"value"})
		
		sense.load_image("smile.png")
	    	print('Button pressed')
		time.sleep(1)
		sense.load_image(currentCompany + ".png")

