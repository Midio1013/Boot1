from machine import Pin
from time import sleep
a=Pin(25,Pin.OUT)
while True:
	a.value(0)
	sleep(1)
	a.value(1)
	sleep(1)