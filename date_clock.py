import datetime as dt
import sys
import time as ti

try:
	while True:
		w=str(dt.datetime.now())
		print(w[0:19])
except KeyboardInterrupt:
	print("\nEnd!")
	ti.sleep(0.14)
	sys.exit()