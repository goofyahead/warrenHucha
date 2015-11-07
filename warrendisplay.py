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
	time.sleep(0.1)

	currentCompany = r.json()["company"]

	if GPIO.event_detected(21):
		update = requests.post("http://warren.ngrok.io/coin", data = {"key":"value"})
		
		sense.load_image("smile.png")
	    	print('Button pressed')

	    sense.load_image(currentCompany + ".png")
	    time.sleep(0.5)

	    if (response.json()["coeficient"] > 1):
			sense.load_image("arrow_up.png")
		else:
			sense.load_image("arrow_down.png")

		sense.show_message("Coins: " + str(response.json()["value"] * response.json()["coeficient"]), text_colour=[0, 255, 0])

		time.sleep(0.5)
		

