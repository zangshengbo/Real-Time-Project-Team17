
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# associate pin 23 to TRIG
TRIG = 23
# associate pin 24 to ECHO
ECHO = 24
print "Distance measurement in progress"
# set pin as GPIO out
GPIO.setup(TRIG,GPIO.OUT)
# set pin as GPIO in
GPIO.setup(ECHO,GPIO.IN)

while True:
	GPIO.output(TRIG, False)
	print "Waitng For Sensor To Settle"
	# delay 2 sec
	time.sleep(2)

	GPIO.output(TRIG, True)
	# delay 0.00001 sec
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	minimum_alert_dis = 7
	maximum_alert_dis = 80
	if distance > 2 and distance < 400:
		print "Distance:",distance - 0.5,"cm"
		if distance >= minimum_alert_dis and distance <= maximum_alert_dis:
			print "Distance alert! Object distance is within ",minimum_alert_dis," and ",maximum_alert_dis,"cm"
	else:
		print "Out Of Range"