import RPi.GPIO as GPIO
import time

# set GPIO board configuration
GPIO.setmode(GPIO.BOARD)

TRIG = 36
ECHO = 32

GPIO.setup(TRIG,GPIO.OUT) # Set variable TRIG AS OUTPUT
GPIO.setup(ECHO,GPIO.IN) # Set variable ECHO as INPUT

GPIO.output(TRIG, False)

# Start sending ultrasonic signal
GPIO.output(TRIG,True)
# waiting time in seconds
time.sleep(0.0001)
# Stop sending the signal
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
while GPIO.input(ECHO)==1:
    pulse_end = time.time()

# Calculate the duration of the pulse
pulse_duration = pulse_end-pulse_start

# Calculate the distance
distance = pulse_duration*17150

# Round to decimal 2
distance  = round(distance,2)

# writing a condition whether the car is present or not
if distance <= 100:        # distance in cm, and it can be adjusted as per our requirement.
    availability = 0
else:
    availability = 1

GPIO.cleanup()
