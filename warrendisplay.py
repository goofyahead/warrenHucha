# coding: utf-8
from sense_hat import SenseHat
import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

sense = SenseHat()
sense.set_rotation(180)
#load initial image if wanted

GPIO.add_event_detect(21, GPIO.FALLING, bouncetime=800)  # add rising edge detection on a channel
currentCompany = "none"
time_elapsed = 0

while True:
	time.sleep(0.1)

	if GPIO.event_detected(21):
		sense.load_image("smile.png")
		response = requests.post("http://warren.ngrok.io/coin", data = {"key":"value"})
		
	    	time.sleep(1)
		print('Button pressed')
		sense.load_image(response.json()["selectedCompany"] + ".png")
		time.sleep(1)

		if (float(response.json()["coeficient"]) > 1):
			sense.load_image("arrow_up.png")
			time.sleep(1)
		else:
			sense.load_image("arrow_down.png")
			time.sleep(1)
		
		sense.show_message(str( int(response.json()["value"]) * float(response.json()["coeficient"]) ) + "e", text_colour=[0, 255, 0])
		

