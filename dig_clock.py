import time
import datetime
import sys

while True:
	try:
		print(time.time())
	except KeyboardInterrupt:
		sys.exit()